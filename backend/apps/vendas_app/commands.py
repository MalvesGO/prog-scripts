# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaebusiness.gaeutil import SaveCommand, ModelSearchCommand
from gaeforms.ndb.form import ModelForm
from gaegraph.business_base import UpdateNode
from vendas_app.model import Venda

class VendaPublicForm(ModelForm):
    """
    Form used to show properties on app's home
    """
    _model_class = Venda
    _include = [Venda.numero_dormitorios, 
                Venda.detalhes, 
                Venda.forma_pg, 
                Venda.bairro, 
                Venda.vaga_garagem, 
                Venda.rua, 
                Venda.area_total, 
                Venda.nome_responsavel, 
                Venda.numero, 
                Venda.valor, 
                Venda.cep, 
                Venda.tipo_imovel, 
                Venda.area_construida, 
                Venda.cpf_responsavel]


class VendaForm(ModelForm):
    """
    Form used to save and update operations on app's admin page
    """
    _model_class = Venda
    _include = [Venda.numero_dormitorios, 
                Venda.detalhes, 
                Venda.forma_pg, 
                Venda.bairro, 
                Venda.vaga_garagem, 
                Venda.rua, 
                Venda.area_total, 
                Venda.nome_responsavel, 
                Venda.numero, 
                Venda.valor, 
                Venda.cep, 
                Venda.tipo_imovel, 
                Venda.area_construida, 
                Venda.cpf_responsavel]


class VendaDetailForm(ModelForm):
    """
    Form used to show entity details on app's admin page
    """
    _model_class = Venda
    _include = [Venda.numero_dormitorios, 
                Venda.creation, 
                Venda.detalhes, 
                Venda.forma_pg, 
                Venda.bairro, 
                Venda.vaga_garagem, 
                Venda.rua, 
                Venda.area_total, 
                Venda.nome_responsavel, 
                Venda.numero, 
                Venda.valor, 
                Venda.cpf_responsavel, 
                Venda.tipo_imovel, 
                Venda.area_construida, 
                Venda.cep]


class VendaShortForm(ModelForm):
    """
    Form used to show entity short version on app's admin page, mainly for tables
    """
    _model_class = Venda
    _include = [Venda.numero_dormitorios, 
                Venda.creation, 
                Venda.detalhes, 
                Venda.forma_pg, 
                Venda.bairro, 
                Venda.vaga_garagem, 
                Venda.rua, 
                Venda.area_total, 
                Venda.nome_responsavel, 
                Venda.numero, 
                Venda.valor, 
                Venda.cpf_responsavel, 
                Venda.tipo_imovel, 
                Venda.area_construida, 
                Venda.cep]


class SaveVendaCommand(SaveCommand):
    _model_form_class = VendaForm


class UpdateVendaCommand(UpdateNode):
    _model_form_class = VendaForm


class ListVendaCommand(ModelSearchCommand):
    def __init__(self):
        super(ListVendaCommand, self).__init__(Venda.query_by_creation())

