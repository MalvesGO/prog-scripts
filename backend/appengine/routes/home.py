# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
import random
from config.template_middleware import TemplateResponse
from routes.imoveis.home import Imovel, ImovelFormTable
from tekton import router
from gaecookie.decorator import no_csrf
from gaepermission.decorator import login_not_required
from locacao_app import facade_locacaos
from venda_app import facade


@login_not_required
@no_csrf
def index():

    query = Imovel.query().order()
    imovel_lista = query.fetch()
    imovel_form=ImovelFormTable()
    imovel_lista=[imovel_form.fill_with_model(imovel) for imovel in imovel_lista]

    contexto = {'imovel_lista':imovel_lista}

    return TemplateResponse(contexto)

