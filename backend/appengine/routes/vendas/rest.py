# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaebusiness.business import CommandExecutionException
from tekton.gae.middleware.json_middleware import JsonResponse
from venda_app import facade


def index():
    cmd = facade.list_vendas_cmd()
    venda_list = cmd()
    short_form=facade.venda_short_form()
    venda_short = [short_form.fill_with_model(m) for m in venda_list]
    return JsonResponse(venda_short)


def save(**venda_properties):
    cmd = facade.save_venda_cmd(**venda_properties)
    return _save_or_update_json_response(cmd)


def update(venda_id, **venda_properties):
    cmd = facade.update_venda_cmd(venda_id, **venda_properties)
    return _save_or_update_json_response(cmd)


def delete(venda_id):
    facade.delete_venda_cmd(venda_id)()


def _save_or_update_json_response(cmd):
    try:
        venda = cmd()
    except CommandExecutionException:
        return JsonResponse({'errors': cmd.errors})
    short_form=facade.venda_short_form()
    return JsonResponse(short_form.fill_with_model(venda))

