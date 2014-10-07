# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaebusiness.business import CommandExecutionException
from tekton.gae.middleware.json_middleware import JsonResponse
from cliente_app import facade


def index():
    cmd = facade.list_clientes_cmd()
    cliente_list = cmd()
    short_form=facade.cliente_short_form()
    cliente_short = [short_form.fill_with_model(m) for m in cliente_list]
    return JsonResponse(cliente_short)


def save(**cliente_properties):
    cmd = facade.save_cliente_cmd(**cliente_properties)
    return _save_or_update_json_response(cmd)


def update(cliente_id, **cliente_properties):
    cmd = facade.update_cliente_cmd(cliente_id, **cliente_properties)
    return _save_or_update_json_response(cmd)


def delete(cliente_id):
    facade.delete_cliente_cmd(cliente_id)()


def _save_or_update_json_response(cmd):
    try:
        cliente = cmd()
    except CommandExecutionException:
        return JsonResponse({'errors': cmd.errors})
    short_form=facade.cliente_short_form()
    return JsonResponse(short_form.fill_with_model(cliente))

