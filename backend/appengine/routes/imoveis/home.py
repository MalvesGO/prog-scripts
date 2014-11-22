# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from google.appengine.ext import ndb
from cliente_app.model import Cliente
from config.template_middleware import TemplateResponse
from gaecookie.decorator import no_csrf
from gaeforms.ndb.form import ModelForm
from gaegraph.model import Arc, Node
from gaepermission.decorator import login_not_required, permissions
from permission_app.model import ADMIN, CORRETOR
from tekton import router
from tekton.gae.middleware.redirect import RedirectResponse

@permissions(ADMIN, CORRETOR)
@no_csrf
def index():
    query = Imovel.query().order(Imovel.creation)
    imoveis = query.fetch()
    contexto = {'imoveis':imoveis}
    return TemplateResponse(contexto)

@permissions(ADMIN, CORRETOR)
@no_csrf
def exibir(cliente_id):
    cliente = Cliente.get_by_id(int(cliente_id))
    query=ClienteImovel.query(ClienteImovel.origin==cliente.key)
    lista_de_imoveis=query.fetch()
    chaves_de_imoveis = [arco.destination for arco in lista_de_imoveis]
    imoveis=ndb.get_multi(chaves_de_imoveis)
    imovel_form = ImovelFormTable()
    imoveis = [imovel_form.fill_with_model(imovel) for imovel in imoveis]
    edit_path = router.to_path(form_edicao)
    remove_path = router.to_path(deletar)
    for imovel in imoveis:
        imovel['edit_path'] = '%s/%s/%s' % (edit_path, cliente_id, imovel['id'])
        imovel['remove_path'] = '%s/%s/%s' % (remove_path, cliente_id, imovel['id'])

    contexto = {'imoveis_lista':imoveis,
                'cliente': cliente,
                'new_imovel':router.to_path(novo, cliente_id)}

    return TemplateResponse(contexto, 'imoveis/exibir_imoveis.html')


@permissions(ADMIN, CORRETOR)
@no_csrf
def novo(cliente_id):
    cliente = Cliente.get_by_id(int(cliente_id))
    query=ClienteImovel.query(ClienteImovel.destination==cliente.key)
    lista_de_imoveis=query.fetch()
    chaves_de_imoveis = [arco.destination for arco in lista_de_imoveis]
    imoveis=ndb.get_multi(chaves_de_imoveis)
    imovel_form = ImovelFormTable()
    imoveis_dcts = [imovel_form.fill_with_model(imovel) for imovel in imoveis]

    contexto = {'imoveis_lista':imoveis_dcts,
                'cliente': cliente,
                'save_path':router.to_path(salvar, cliente_id)}

    return TemplateResponse(contexto, 'imoveis/imoveis.html')

@permissions(ADMIN, CORRETOR)
def salvar(cliente_id, **propriedades):
    cliente_chave = Cliente.get_by_id(int(cliente_id))
    imovel_form = ImovelForm(**propriedades)
    errors = imovel_form.validate()
    if errors:
        contexto = {'save_path':router.to_path(salvar, cliente_id),
                    'errors':errors,
                    'cliente':Cliente.get_by_id(int(cliente_id)),
                    'imovel':imovel_form}
        return TemplateResponse(contexto, '/imoveis/imoveis.html')
    else:
        imovel = imovel_form.fill_model()
        imovel_chave = imovel.put()
        cliente_imovel = ClienteImovel(origin=cliente_chave, destination=imovel_chave)
        cliente_imovel.put()
        return RedirectResponse(router.to_path(exibir, cliente_id))

@permissions(ADMIN, CORRETOR)
@no_csrf
def form_edicao(cliente_id, imovel_id):
    imovel_id = int(imovel_id)
    imovel = Imovel.get_by_id(imovel_id)
    imovel_form = ImovelForm()
    imovel_dct = imovel_form.fill_with_model(imovel)
    contexto = {'save_path': router.to_path(editar, cliente_id, imovel_id),
                'imovel': imovel_dct}
    return TemplateResponse(contexto, 'imoveis/edit_imoveis.html')

@permissions(ADMIN, CORRETOR)
def editar(cliente_id, imovel_id, **propriedades):
    imovel_form = ImovelForm(**propriedades)
    errors = imovel_form.validate()
    if errors:
        contexto = {'save_path': router.to_path(editar, cliente_id, imovel_id),
                    'errors': errors,
                    'imovel': propriedades}
        return TemplateResponse(contexto, 'imoveis/edit_imoveis.html')
    imovel = Imovel.get_by_id(int(imovel_id))
    imovel_form.fill_model(imovel)
    imovel.put()
    return RedirectResponse(router.to_path(exibir, cliente_id))

@permissions(ADMIN, CORRETOR)
def deletar(cliente_id, imovel_id):
    imovel_chave = ndb.Key(Imovel, int(imovel_id))
    futuro = imovel_chave.delete_async()
    query = ClienteImovel.find_origins(imovel_chave)
    chaves_a_serem_apagadas = query.fetch(keys_only=True)
    chaves_a_serem_apagadas.append(imovel_chave)
    ndb.delete_multi(chaves_a_serem_apagadas)
    futuro.get_result()
    return RedirectResponse(router.to_path(exibir, cliente_id))

# Modelo e formulário

class Imovel(Node):
    cep = ndb.StringProperty(required=True)
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
                Imovel.tipo, Imovel.transacao, Imovel.area_util, Imovel.vagas, Imovel.dormitorios,
                Imovel.area_terreno, Imovel.valor]

class ClienteImovel(Arc):
    origin = ndb.KeyProperty(Cliente, required=True) # Chave que irá referenciar o usuário
    destination = ndb.KeyProperty(Imovel, required=True) # Chave que irá referenciar o imóvel
