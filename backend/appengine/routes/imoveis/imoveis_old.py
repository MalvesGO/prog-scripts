from google.appengine.ext import ndb
from cliente_app.commands import ClienteForm
from cliente_app.model import Cliente
from config.template_middleware import TemplateResponse
from gaecookie.decorator import no_csrf
from gaeforms.ndb.form import ModelForm
from gaepermission.decorator import permissions
from gaegraph.model import Node, Arc
from permission_app.model import ADMIN, CORRETOR, CLIENTE
from tekton import router
from tekton.gae.middleware.redirect import RedirectResponse

class Imovel(Node):
    cep=ndb.StringProperty(required=True)
    endereco=ndb.StringProperty(required=True)
    numero=ndb.IntegerProperty(required=True)
    complemento=ndb.StringProperty()
    bairro=ndb.StringProperty(required=True)
    cidade=ndb.StringProperty(required=True)
    estado=ndb.StringProperty(required=True)
    categoria=ndb.StringProperty(required=True)
    tipo=ndb.StringProperty(required=True)
    subtipo=ndb.StringProperty()
    transacao=ndb.StringProperty(required=True)
    area_util=ndb.IntegerProperty(required=True)
    area_terreno=ndb.IntegerProperty(required=True)
    vagas=ndb.IntegerProperty(required=True)
    dormitorios=ndb.IntegerProperty(required=True)
    suites=ndb.IntegerProperty(required=True)
    salas=ndb.IntegerProperty(required=True)
    copas=ndb.IntegerProperty(required=True)
    cozinhas=ndb.IntegerProperty(required=True)
    descricao=ndb.StringProperty()
    valor=ndb.FloatProperty(required=True)
    valor_condominio=ndb.FloatProperty()


class ImovelForm(ModelForm):
    _model_class = Imovel
    _include = [Imovel.cep, Imovel.endereco, Imovel.numero, Imovel.complemento,
                Imovel.bairro, Imovel.cidade, Imovel.estado, Imovel.categoria,
                Imovel.tipo, Imovel.subtipo, Imovel.transacao, Imovel.area_util,
                Imovel.area_terreno, Imovel.vagas,
                Imovel.dormitorios, Imovel.suites, Imovel.salas,
                Imovel.copas, Imovel.cozinhas, Imovel.descricao,
                Imovel.valor, Imovel.valor_condominio]

class ImovelFormTable(ModelForm):
    _model_class = Imovel
    _include = [Imovel.cep, Imovel.endereco,  Imovel.bairro,
                Imovel.cidade, Imovel.estado, Imovel.categoria,
                Imovel.tipo, Imovel.transacao, Imovel.area_util,
                Imovel.area_terreno, Imovel.valor]

@permissions(ADMIN, CORRETOR, CLIENTE)
@no_csrf
def index():
    query = Imovel.query().order()
    imovel_lista = query.fetch()
    imovel_form=ImovelFormTable()
    imovel_lista=[imovel_form.fill_with_model(imovel) for imovel in imovel_lista]
    editar_form_path = router.to_path(editar_form)
    delete_path = router.to_path(delete)
    for imovel in imovel_lista:
        imovel['edit_path'] = '%s/%s' % (editar_form_path, imovel['id'])
        imovel['delete_path'] = '%s/%s' % (delete_path, imovel['id'])
    contexto = {'imovel_lista':imovel_lista,
                'new_imovel': router.to_path(form)}
    return TemplateResponse(contexto )

@permissions(ADMIN, CORRETOR, CLIENTE)
def delete(imovel_id):
    chave=ndb.Key(Imovel, int(imovel_id))
    chave.delete()
    return RedirectResponse(router.to_path(index))

@permissions(ADMIN, CORRETOR, CLIENTE)
@no_csrf
def form():
    contexto = {'save_path':router.to_path(salvar),
                'new_imovel': router.to_path(form)}
    return TemplateResponse(contexto)

@permissions(ADMIN, CORRETOR, CLIENTE)
def salvar(** propriedades):
    imovel_form = ImovelForm(**propriedades)
    errors = imovel_form.validate()
    if errors:
        contexto = {'save_path':router.to_path(salvar),
                    'errors':errors,
                    'imovel':imovel_form}
        return TemplateResponse(contexto, '/imoveis/form.html')
    else:
        imovel = imovel_form.fill_model()
        imovel.put()
        return RedirectResponse(router.to_path(index))

@permissions(ADMIN, CORRETOR, CLIENTE)
@no_csrf
def editar_form(imovel_id):
    imovel_id = int(imovel_id)
    imovel = Imovel.get_by_id(imovel_id)
    imovel_form = ImovelForm()
    imovel_form.fill_with_model(imovel)
    contexto = {'save_path':router.to_path(editar, imovel_id),
                    'imovel':imovel_form}
    return TemplateResponse(contexto, '/imoveis/form.html')

@permissions(ADMIN, CORRETOR, CLIENTE)
def editar(imovel_id, **propriedades):
    imovel_id = int(imovel_id)
    imovel = Imovel.get_by_id(imovel_id)
    imovel_form = ImovelForm(**propriedades)
    errors = imovel_form.validate()
    if errors:
         contexto = {'save_path':router.to_path(salvar),
                    'errors':errors,
                    'imovel':imovel_form}
         return TemplateResponse(contexto, '/imoveis/form.html')
    else:
        imovel_form.fill_model(imovel)
        imovel.put()
        return RedirectResponse(router.to_path(index))
