# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from google.appengine.ext import ndb
from gaegraph.model import Node
from gaeforms.ndb import property


class Cliente(Node):
    nome = ndb.StringProperty(required=True)
    profissao = ndb.StringProperty(required=True)
    estado_civil = ndb.StringProperty(required=True)
    nacionalidade = ndb.StringProperty(required=True)
    nascimento = ndb.DateProperty(required=True)
    rg = ndb.StringProperty(required=True)
    cpf = ndb.StringProperty(required=True)
    cep = ndb.StringProperty(required=True)
    endereco = ndb.StringProperty(required=True)
    numero = ndb.IntegerProperty(required=True)
    complemento = ndb.StringProperty(required=True)
    bairro = ndb.StringProperty(required=True)
    cidade = ndb.StringProperty(required=True)
    estado = ndb.StringProperty(required=True)
    telefone = ndb.StringProperty(required=True)
    celular = ndb.StringProperty(required=True)
    email = ndb.StringProperty(required=True)

