# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from google.appengine.ext import ndb
from gaegraph.model import Node
from gaeforms.ndb import property


class Venda(Node):
    tipo_imovel = ndb.StringProperty(required=True)
    cep = ndb.StringProperty(required=True)

