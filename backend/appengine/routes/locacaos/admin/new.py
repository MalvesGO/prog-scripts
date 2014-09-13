# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from gaebusiness.business import CommandExecutionException
from tekton import router
from gaecookie.decorator import no_csrf
from locacao_app import facade_locacaos
from routes.locacaos import admin


@no_csrf
def index():
    return TemplateResponse({'save_path': router.to_path(save)},'locacaos/admin/form.html')


def save(_handler, locacao_id=None, **locacao_properties):
    cmd = facade_locacaos.save_locacao_cmd(**locacao_properties)
    try:
        cmd()
    except CommandExecutionException:
        context = {'errors': cmd.errors,
                   'locacao': cmd.form}

        return TemplateResponse(context, 'locacaos/admin/form.html')
    _handler.redirect(router.to_path(admin))

