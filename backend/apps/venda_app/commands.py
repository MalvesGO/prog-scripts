# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaebusiness.gaeutil import SaveCommand, ModelSearchCommand
from gaeforms.ndb.form import ModelForm
from gaegraph.business_base import UpdateNode
from venda_app.model import Venda

class VendaPublicForm(ModelForm):
    """
    Form used to show properties on app's home
    """
    _model_class = Venda
    _include = [Venda.tipo_imovel, 
                Venda.cep]


class VendaForm(ModelForm):
    """
    Form used to save and update operations on app's admin page
    """
    _model_class = Venda
    _include = [Venda.tipo_imovel, 
                Venda.cep]


class VendaDetailForm(ModelForm):
    """
    Form used to show entity details on app's admin page
    """
    _model_class = Venda
    _include = [Venda.creation, 
                Venda.tipo_imovel, 
                Venda.cep]


class VendaShortForm(ModelForm):
    """
    Form used to show entity short version on app's admin page, mainly for tables
    """
    _model_class = Venda
    _include = [Venda.creation, 
                Venda.tipo_imovel, 
                Venda.cep]


class SaveVendaCommand(SaveCommand):
    _model_form_class = VendaForm


class UpdateVendaCommand(UpdateNode):
    _model_form_class = VendaForm


class ListVendaCommand(ModelSearchCommand):
    def __init__(self):
        super(ListVendaCommand, self).__init__(Venda.query_by_creation())

