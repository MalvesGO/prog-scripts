# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from gaebusiness.business import CommandExecutionException
from gaepermission.decorator import permissions
from permission_app.model import ADMIN, CORRETOR
from tekton import router
from gaecookie.decorator import no_csrf
from locacao_app import facade_locacaos
from routes.locacaos import admin


@no_csrf
def index(locacao_id):
    locacao = facade_locacaos.get_locacao_cmd(locacao_id)()
    detail_form = facade_locacaos.locacao_detail_form()
    context = {'save_path': router.to_path(save, locacao_id), 'locacao': detail_form.fill_with_model(locacao)}
    return TemplateResponse(context, 'locacaos/admin/form.html')

@permissions(ADMIN, CORRETOR)
def save(_handler, locacao_id, **locacao_properties):
    cmd = facade_locacaos.update_locacao_cmd(locacao_id, **locacao_properties)
    try:
        cmd()
    except CommandExecutionException:
        context = {'errors': cmd.errors,
                   'locacao': cmd.form}

        return TemplateResponse(context, 'locacaos/admin/form.html')
    _handler.redirect(router.to_path(admin))

