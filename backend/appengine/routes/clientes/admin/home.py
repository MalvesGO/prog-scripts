# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from gaepermission.decorator import permissions
from permission_app.model import ADMIN
from tekton import router
from gaecookie.decorator import no_csrf
from cliente_app import facade
from routes.clientes.admin import new, edit

@permissions(ADMIN)
def delete(_handler, cliente_id):
    facade.delete_cliente_cmd(cliente_id)()
    _handler.redirect(router.to_path(index))

@permissions(ADMIN)
@no_csrf
def index():
    cmd = facade.list_clientes_cmd()
    clientes = cmd()
    edit_path = router.to_path(edit)
    delete_path = router.to_path(delete)
    short_form = facade.cliente_short_form()

    def short_cliente_dict(cliente):
        cliente_dct = short_form.fill_with_model(cliente)
        cliente_dct['edit_path'] = router.to_path(edit_path, cliente_dct['id'])
        cliente_dct['delete_path'] = router.to_path(delete_path, cliente_dct['id'])
        return cliente_dct

    short_clientes = [short_cliente_dict(cliente) for cliente in clientes]
    context = {'clientes': short_clientes,
               'new_path': router.to_path(new)}
    return TemplateResponse(context)

