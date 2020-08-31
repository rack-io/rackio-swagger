# -*- coding: utf-8 -*-
"""rackio_swagger/core.py

This module implements the core app class and methods for Rackio Swagger UI.
"""

from falcon_swagger_ui import register_swaggerui_app

from ._singleton import Singleton


class RackioSwagger(Singleton):

    def __init__(self):

        super(RackioSwagger, self).__init__()
        
        self.app = None

        self.SWAGGERUI_URL = '/swagger'
        self.SCHEMA_URL = '/static/swagger.json'

        self.page_title = 'Rackio Swagger Doc'
        self.favicon_url = 'https://falconframework.org/favicon-32x32.png'


    def register_swagger(self):

        api = self.app._api
        url = self.SWAGGERUI_URL
        schema = self.SCHEMA_URL
        title = self.page_title
        favicon = self.favicon_url

        register_swaggerui_app(
            api, url, schema,
            page_title=title,
            favicon_url=favicon,
            config={'supportedSubmitMethods': ['get'], }
        )

    def __call__(self, app):

        self.app = app