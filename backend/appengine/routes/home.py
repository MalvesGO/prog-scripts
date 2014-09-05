# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
import random
from config.template_middleware import TemplateResponse
from tekton import router
from gaecookie.decorator import no_csrf
from gaepermission.decorator import login_not_required
from venda_app import facade
from routes.vendas import admin
from locacao_app import facade_locacao
from routes.locacaos import admin_locacao

@login_not_required
@no_csrf
def index():

    cmd = facade.list_vendas_cmd()
    vendas = cmd()
    public_form = facade.venda_public_form()
    venda_public_dcts = [public_form.fill_with_model(venda) for venda in vendas]

    cmd_locacao = facade_locacao.list_locacaos_cmd()
    locacaos = cmd_locacao()
    public_form_locacao = facade_locacao.locacao_public_form()
    locacao_public_dcts = [public_form_locacao.fill_with_model(locacao) for locacao in locacaos]

    context = {'vendas': venda_public_dcts, 'locacaos': locacao_public_dcts }

    return TemplateResponse(context)

