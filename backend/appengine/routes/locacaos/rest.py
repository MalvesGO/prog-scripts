# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaebusiness.business import CommandExecutionException
from tekton.gae.middleware.json_middleware import JsonResponse
from locacao_app import facade


def index():
    cmd = facade.list_locacaos_cmd()
    locacao_list = cmd()
    short_form=facade.locacao_short_form()
    locacao_short = [short_form.fill_with_model(m) for m in locacao_list]
    return JsonResponse(locacao_short)


def save(**locacao_properties):
    cmd = facade.save_locacao_cmd(**locacao_properties)
    return _save_or_update_json_response(cmd)


def update(locacao_id, **locacao_properties):
    cmd = facade.update_locacao_cmd(locacao_id, **locacao_properties)
    return _save_or_update_json_response(cmd)


def delete(locacao_id):
    facade.delete_locacao_cmd(locacao_id)()


def _save_or_update_json_response(cmd):
    try:
        locacao = cmd()
    except CommandExecutionException:
        return JsonResponse({'errors': cmd.errors})
    short_form=facade.locacao_short_form()
    return JsonResponse(short_form.fill_with_model(locacao))

