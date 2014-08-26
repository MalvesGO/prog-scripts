# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaegraph.business_base import NodeSearch, DeleteNode
from vendas_app.commands import ListVendaCommand, SaveVendaCommand, UpdateVendaCommand, \
    VendaPublicForm, VendaDetailForm, VendaShortForm


def save_venda_cmd(**venda_properties):
    """
    Command to save Venda entity
    :param venda_properties: a dict of properties to save on model
    :return: a Command that save Venda, validating and localizing properties received as strings
    """
    return SaveVendaCommand(**venda_properties)


def update_venda_cmd(venda_id, **venda_properties):
    """
    Command to update Venda entity with id equals 'venda_id'
    :param venda_properties: a dict of properties to update model
    :return: a Command that update Venda, validating and localizing properties received as strings
    """
    return UpdateVendaCommand(venda_id, **venda_properties)


def list_vendas_cmd():
    """
    Command to list Venda entities ordered by their creation dates
    :return: a Command proceed the db operations when executed
    """
    return ListVendaCommand()


def venda_detail_form(**kwargs):
    """
    Function to get Venda's detail form.
    :param kwargs: form properties
    :return: Form
    """
    return VendaDetailForm(**kwargs)


def venda_short_form(**kwargs):
    """
    Function to get Venda's short form. just a subset of venda's properties
    :param kwargs: form properties
    :return: Form
    """
    return VendaShortForm(**kwargs)

def venda_public_form(**kwargs):
    """
    Function to get Venda'spublic form. just a subset of venda's properties
    :param kwargs: form properties
    :return: Form
    """
    return VendaPublicForm(**kwargs)


def get_venda_cmd(venda_id):
    """
    Find venda by her id
    :param venda_id: the venda id
    :return: Command
    """
    return NodeSearch(venda_id)


def delete_venda_cmd(venda_id):
    """
    Construct a command to delete a Venda
    :param venda_id: venda's id
    :return: Command
    """
    return DeleteNode(venda_id)

