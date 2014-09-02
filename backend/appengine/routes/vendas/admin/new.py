# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from gaebusiness.business import CommandExecutionException
from tekton import router
from gaecookie.decorator import no_csrf
from venda_app import facade
from routes.vendas import admin
from gaepermission import facade
from gaepermission.decorator import permissions
from permission_app.model import ALL_PERMISSIONS_LIST, ADMIN,CORRETOR

@no_csrf
def index():
    return TemplateResponse({'save_path': router.to_path(save)},'vendas/admin/form.html')

def save(_handler, venda_id=None, **venda_properties):
    cmd = facade.save_venda_cmd(**venda_properties)
    try:
        cmd()
    except CommandExecutionException:
        context = {'errors': cmd.errors,
                   'venda': cmd.form}

        return TemplateResponse(context, 'vendas/admin/form.html')
    _handler.redirect(router.to_path(admin))

