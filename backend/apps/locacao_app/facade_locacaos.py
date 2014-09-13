# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaegraph.business_base import NodeSearch, DeleteNode
from locacao_app.commands import ListLocacaoCommand, SaveLocacaoCommand, UpdateLocacaoCommand, \
    LocacaoPublicForm, LocacaoDetailForm, LocacaoShortForm


def save_locacao_cmd(**locacao_properties):
    """
    Command to save Locacao entity
    :param locacao_properties: a dict of properties to save on model
    :return: a Command that save Locacao, validating and localizing properties received as strings
    """
    return SaveLocacaoCommand(**locacao_properties)


def update_locacao_cmd(locacao_id, **locacao_properties):
    """
    Command to update Locacao entity with id equals 'locacao_id'
    :param locacao_properties: a dict of properties to update model
    :return: a Command that update Locacao, validating and localizing properties received as strings
    """
    return UpdateLocacaoCommand(locacao_id, **locacao_properties)


def list_locacaos_cmd():
    """
    Command to list Locacao entities ordered by their creation dates
    :return: a Command proceed the db operations when executed
    """
    return ListLocacaoCommand()


def locacao_detail_form(**kwargs):
    """
    Function to get Locacao's detail form.
    :param kwargs: form properties
    :return: Form
    """
    return LocacaoDetailForm(**kwargs)


def locacao_short_form(**kwargs):
    """
    Function to get Locacao's short form. just a subset of locacao's properties
    :param kwargs: form properties
    :return: Form
    """
    return LocacaoShortForm(**kwargs)

def locacao_public_form(**kwargs):
    """
    Function to get Locacao'spublic form. just a subset of locacao's properties
    :param kwargs: form properties
    :return: Form
    """
    return LocacaoPublicForm(**kwargs)


def get_locacao_cmd(locacao_id):
    """
    Find locacao by her id
    :param locacao_id: the locacao id
    :return: Command
    """
    return NodeSearch(locacao_id)


def delete_locacao_cmd(locacao_id):
    """
    Construct a command to delete a Locacao
    :param locacao_id: locacao's id
    :return: Command
    """
    return DeleteNode(locacao_id)

