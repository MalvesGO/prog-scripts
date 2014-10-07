# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from routes.clientes.home import Imovel, ImovelFormTable
from tekton import router
from gaecookie.decorator import no_csrf
from gaepermission.decorator import login_not_required
from locacao_app import facade_locacaos
from routes.locacaos import admin


@login_not_required
@no_csrf
def index():
    #cmd = facade_locacaos.list_locacaos_cmd()
    #locacaos = cmd()
    #public_form = facade_locacaos.locacao_public_form()
    #locacao_public_dcts = [public_form.fill_with_model(locacao) for locacao in locacaos]
    #context = {'locacaos': locacao_public_dcts,'admin_path':router.to_path(admin)}

    query = Imovel.query().order()
    imovel_lista = query.fetch()
    imovel_form=ImovelFormTable()
    imovel_lista=[imovel_form.fill_with_model(imovel) for imovel in imovel_lista]

    contexto = {'imovel_lista':imovel_lista}
    return TemplateResponse(contexto)

