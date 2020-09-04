# -*- coding: utf-8 -*-
"""rackio_swagger/schema.py

This module implements the schema dict to produce the json schema.
"""
import copy

from deepmerge import always_merger

from ._singleton import Singleton
from .spec import swagger


class SchemaManager(Singleton):

    def __init__(self):

        super(SchemaManager, self).__init__()

        self._schema = copy.deepcopy(swagger)

    def get_schema(self):

        return self._schema

    def merge_schema(self, schema):

        self._schema = always_merger.merge(self._schema, schema)

def get_schema():

    
    manager = SchemaManager()

    return manager.get_schema()