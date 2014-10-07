# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from routes.clientes.home import Imovel, ImovelFormTable
from tekton import router
from gaecookie.decorator import no_csrf
from gaepermission.decorator import login_not_required
from venda_app import facade
from routes.vendas import admin


@login_not_required
@no_csrf
def index():
    #cmd = facade.list_vendas_cmd()
    #vendas = cmd()
    #public_form = facade.venda_public_form()
    #venda_public_dcts = [public_form.fill_with_model(venda) for venda in vendas]
    #context = {'vendas': venda_public_dcts,'admin_path':router.to_path(admin)}

    query = Imovel.query().order()
    imovel_lista = query.fetch()
    imovel_form=ImovelFormTable()
    imovel_lista=[imovel_form.fill_with_model(imovel) for imovel in imovel_lista]

    contexto = {'imovel_lista':imovel_lista}
    return TemplateResponse(contexto)

