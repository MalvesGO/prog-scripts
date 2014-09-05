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
from permission_app.model import ALL_PERMISSIONS_LIST, ADMIN, CORRETOR

@no_csrf
def index(venda_id):
    venda = facade.get_venda_cmd(venda_id)()
    detail_form = facade.venda_detail_form()
    context = {'save_path': router.to_path(save, venda_id), 'venda': detail_form.fill_with_model(venda)}
    return TemplateResponse(context, 'vendas/admin_locacao/form.html')


def save(_handler, venda_id, **venda_properties):
    cmd = facade.update_venda_cmd(venda_id, **venda_properties)
    try:
        cmd()
    except CommandExecutionException:
        context = {'errors': cmd.errors,
                   'venda': cmd.form}

        return TemplateResponse(context, 'vendas/admin_locacao/form.html')
    _handler.redirect(router.to_path(admin))

