# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from gaepermission.decorator import permissions
from permission_app.model import ADMIN, CORRETOR
from tekton import router
from gaecookie.decorator import no_csrf
from venda_app import facade
from routes.vendas.admin import new, edit


def delete(_handler, venda_id):
    facade.delete_venda_cmd(venda_id)()
    _handler.redirect(router.to_path(index))

@permissions(ADMIN, CORRETOR)
@no_csrf
def index():
    cmd = facade.list_vendas_cmd()
    vendas = cmd()
    edit_path = router.to_path(edit)
    delete_path = router.to_path(delete)
    short_form = facade.venda_short_form()

    def short_venda_dict(venda):
        venda_dct = short_form.fill_with_model(venda)
        venda_dct['edit_path'] = router.to_path(edit_path, venda_dct['id'])
        venda_dct['delete_path'] = router.to_path(delete_path, venda_dct['id'])
        return venda_dct

    short_vendas = [short_venda_dict(venda) for venda in vendas]
    context = {'vendas': short_vendas,
               'new_path': router.to_path(new)}
    return TemplateResponse(context)

