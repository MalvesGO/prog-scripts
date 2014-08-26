# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from tekton import router
from gaecookie.decorator import no_csrf
from gaepermission.decorator import login_not_required
from locacao_app import facade
from routes.locacaos import admin


@login_not_required
@no_csrf
def index():
    cmd = facade.list_locacaos_cmd()
    locacaos = cmd()
    public_form = facade.locacao_public_form()
    locacao_public_dcts = [public_form.fill_with_model(locacao) for locacao in locacaos]
    context = {'locacaos': locacao_public_dcts,'admin_path':router.to_path(admin)}
    return TemplateResponse(context)

