# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from tekton import router
from gaecookie.decorator import no_csrf
from locacao_app import facade_locacaos
from routes.locacaos.admin import new, edit


def delete(_handler, locacao_id):
    facade_locacaos.delete_locacao_cmd(locacao_id)()
    _handler.redirect(router.to_path(index))


@no_csrf
def index():
    cmd = facade_locacaos.list_locacaos_cmd()
    locacaos = cmd()
    edit_path = router.to_path(edit)
    delete_path = router.to_path(delete)
    short_form = facade_locacaos.locacao_short_form()

    def short_locacao_dict(locacao):
        locacao_dct = short_form.fill_with_model(locacao)
        locacao_dct['edit_path'] = router.to_path(edit_path, locacao_dct['id'])
        locacao_dct['delete_path'] = router.to_path(delete_path, locacao_dct['id'])
        return locacao_dct

    short_locacaos = [short_locacao_dict(locacao) for locacao in locacaos]
    context = {'locacaos': short_locacaos,
               'new_path': router.to_path(new)}
    return TemplateResponse(context)

