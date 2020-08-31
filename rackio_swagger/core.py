# -*- coding: utf-8 -*-
"""rackio_swagger/core.py

This module implements the core app class and methods for Rackio Swagger UI.
"""

from ._singleton import Singleton

class RackioSwagger(Singleton):

    def __init__(self):

        super(RackioSwagger, self).__init__()

    def __call__(self):

        pass