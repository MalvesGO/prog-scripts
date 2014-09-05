# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaebusiness.gaeutil import SaveCommand, ModelSearchCommand
from gaeforms.ndb.form import ModelForm
from gaegraph.business_base import UpdateNode
from locacao_app.model import Locacao

class LocacaoPublicForm(ModelForm):
    """
    Form used to show properties on app's home
    """
    _model_class = Locacao
    _include = [Locacao.numero_dormitorios, 
                Locacao.detalhes, 
                Locacao.cpf_responsavel, 
                Locacao.bairro, 
                Locacao.vaga_garagem, 
                Locacao.rua, 
                Locacao.area_total, 
                Locacao.nome_responsavel, 
                Locacao.numero, 
                Locacao.valor, 
                Locacao.cep, 
                Locacao.tipo_imovel, 
                Locacao.area_construida]


class LocacaoForm(ModelForm):
    """
    Form used to save and update operations on app's admin_locacao page
    """
    _model_class = Locacao
    _include = [Locacao.numero_dormitorios, 
                Locacao.detalhes, 
                Locacao.cpf_responsavel, 
                Locacao.bairro, 
                Locacao.vaga_garagem, 
                Locacao.rua, 
                Locacao.area_total, 
                Locacao.nome_responsavel, 
                Locacao.numero, 
                Locacao.valor, 
                Locacao.cep, 
                Locacao.tipo_imovel, 
                Locacao.area_construida]


class LocacaoDetailForm(ModelForm):
    """
    Form used to show entity details on app's admin_locacao page
    """
    _model_class = Locacao
    _include = [Locacao.numero_dormitorios, 
                Locacao.creation, 
                Locacao.detalhes, 
                Locacao.cpf_responsavel, 
                Locacao.bairro, 
                Locacao.vaga_garagem, 
                Locacao.rua, 
                Locacao.area_total, 
                Locacao.nome_responsavel, 
                Locacao.numero, 
                Locacao.valor, 
                Locacao.tipo_imovel, 
                Locacao.area_construida, 
                Locacao.cep]


class LocacaoShortForm(ModelForm):
    """
    Form used to show entity short version on app's admin_locacao page, mainly for tables
    """
    _model_class = Locacao
    _include = [Locacao.numero_dormitorios, 
                Locacao.creation, 
                Locacao.detalhes, 
                Locacao.cpf_responsavel, 
                Locacao.bairro, 
                Locacao.vaga_garagem, 
                Locacao.rua, 
                Locacao.area_total, 
                Locacao.nome_responsavel, 
                Locacao.numero, 
                Locacao.valor, 
                Locacao.tipo_imovel, 
                Locacao.area_construida, 
                Locacao.cep]


class SaveLocacaoCommand(SaveCommand):
    _model_form_class = LocacaoForm


class UpdateLocacaoCommand(UpdateNode):
    _model_form_class = LocacaoForm


class ListLocacaoCommand(ModelSearchCommand):
    def __init__(self):
        super(ListLocacaoCommand, self).__init__(Locacao.query_by_creation())

