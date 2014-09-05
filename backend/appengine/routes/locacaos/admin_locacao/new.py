# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from gaebusiness.business import CommandExecutionException
from tekton import router
from gaecookie.decorator import no_csrf
from locacao_app import facade_locacao
from routes.locacaos import admin_locacao


@no_csrf
def index():
    return TemplateResponse({'save_path': router.to_path(save)},'locacaos/admin_locacao/form.html')


def save(_handler, locacao_id=None, **locacao_properties):
    cmd = facade_locacao.save_locacao_cmd(**locacao_properties)
    try:
        cmd()
    except CommandExecutionException:
        context = {'errors': cmd.errors,
                   'locacao': cmd.form}

        return TemplateResponse(context, 'locacaos/admin_locacao/form.html')
    _handler.redirect(router.to_path(admin_locacao))

