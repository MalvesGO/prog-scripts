# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from google.appengine.ext import ndb
from gaeforms.ndb.form import ModelForm
from gaegraph.model import Node
from gaeforms.ndb import property


class Venda(Node):
    tipo_imovel = ndb.StringProperty(required=True)
    cep = ndb.StringProperty(required=True)
    bairro = ndb.StringProperty(required=True)
    rua = ndb.StringProperty(required=True)
    numero = ndb.IntegerProperty(required=True)
    valor = ndb.FloatProperty(required=True)
    numero_dormitorios = ndb.IntegerProperty(required=True)
    area_construida = ndb.IntegerProperty(required=True)
    area_total = ndb.IntegerProperty(required=True)
    detalhes = ndb.StringProperty
    forma_pg = ndb.StringProperty(required=True)
    vaga_garagem = ndb.IntegerProperty(required=True)
    cpf_responsavel = ndb.StringProperty(required=True)
    nome_responsavel = ndb.StringProperty(required=True)

class VendaForm(ModelForm):
    _model_class = Venda
    _include = [Venda.tipo_imovel, Venda.cep, Venda.bairro, Venda.rua, Venda.numero, Venda.valor, Venda.numero_dormitorios,
                Venda.area_construida, Venda.area_total, Venda.forma_pg, Venda.vaga_garagem, Venda.cpf_responsavel,
                Venda.nome_responsavel]