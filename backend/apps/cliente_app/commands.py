# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaebusiness.gaeutil import SaveCommand, ModelSearchCommand
from gaeforms.ndb.form import ModelForm
from gaegraph.business_base import UpdateNode
from cliente_app.model import Cliente

class ClientePublicForm(ModelForm):
    """
    Form used to show properties on app's home
    """
    _model_class = Cliente
    _include = [Cliente.complemento, 
                Cliente.nome, 
                Cliente.bairro, 
                Cliente.cidade, 
                Cliente.nascimento, 
                Cliente.profissao, 
                Cliente.numero, 
                Cliente.nacionalidade, 
                Cliente.cpf, 
                Cliente.rg, 
                Cliente.celular, 
                Cliente.telefone, 
                Cliente.cep, 
                Cliente.endereco, 
                Cliente.estado_civil, 
                Cliente.estado, 
                Cliente.email]


class ClienteForm(ModelForm):
    """
    Form used to save and update operations on app's admin page
    """
    _model_class = Cliente
    _include = [Cliente.complemento, 
                Cliente.nome, 
                Cliente.bairro, 
                Cliente.cidade, 
                Cliente.nascimento, 
                Cliente.profissao, 
                Cliente.numero, 
                Cliente.nacionalidade, 
                Cliente.cpf, 
                Cliente.rg, 
                Cliente.celular, 
                Cliente.telefone, 
                Cliente.cep, 
                Cliente.endereco, 
                Cliente.estado_civil, 
                Cliente.estado, 
                Cliente.email]


class ClienteDetailForm(ModelForm):
    """
    Form used to show entity details on app's admin page
    """
    _model_class = Cliente
    _include = [Cliente.complemento, 
                Cliente.nome, 
                Cliente.bairro, 
                Cliente.cidade, 
                Cliente.creation, 
                Cliente.profissao, 
                Cliente.numero, 
                Cliente.nacionalidade, 
                Cliente.nascimento, 
                Cliente.rg, 
                Cliente.celular, 
                Cliente.telefone, 
                Cliente.cep, 
                Cliente.endereco, 
                Cliente.estado_civil, 
                Cliente.estado, 
                Cliente.email, 
                Cliente.cpf]


class ClienteShortForm(ModelForm):
    """
    Form used to show entity short version on app's admin page, mainly for tables
    """
    _model_class = Cliente
    _include = [Cliente.complemento, 
                Cliente.nome, 
                Cliente.bairro, 
                Cliente.cidade, 
                Cliente.creation, 
                Cliente.profissao, 
                Cliente.numero, 
                Cliente.nacionalidade, 
                Cliente.nascimento, 
                Cliente.rg, 
                Cliente.celular, 
                Cliente.telefone, 
                Cliente.cep, 
                Cliente.endereco, 
                Cliente.estado_civil, 
                Cliente.estado, 
                Cliente.email, 
                Cliente.cpf]


class SaveClienteCommand(SaveCommand):
    _model_form_class = ClienteForm


class UpdateClienteCommand(UpdateNode):
    _model_form_class = ClienteForm


class ListClienteCommand(ModelSearchCommand):
    def __init__(self):
        super(ListClienteCommand, self).__init__(Cliente.query_by_creation())

