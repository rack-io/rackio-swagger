# -*- coding: utf-8 -*-
"""rackio_swagger/core.py

This module implements the core app class and methods for Rackio Swagger UI.
"""

import json

from falcon_swagger_ui import register_swaggerui_app
from ._singleton import Singleton


class SwaggerCore(Singleton):

    def __init__(self):

        super(SwaggerCore, self).__init__()
        
        self.app = None

        self.SWAGGERUI_URL = '/swagger'
        # self.SCHEMA_URL = 'http://petstore.swagger.io/v2/swagger.json'
        self.SCHEMA_URL = '/swagger/swagger.json'

        self.page_title = 'Rackio Swagger Doc'
        self.favicon_url = 'https://falconframework.org/favicon-32x32.png'

    def core_swagger(self):

        swagger = {
            "swagger": "2.0",
            "basePath": "/api",
            "paths": {
                "/tags": {
                    "get": {
                        "responses": {
                            200: {
                                "description": "Success"
                            }
                        },
                        "tags": ["tags"]
                    }
                },
                "/tags/{tag_id}": {
                    "get": {
                        "responses": {
                            200: {
                                "description": "Success"
                            }
                        },
                        "parameters": [
                            {
                                "name": "tag_id",
                                "required": True,
                                "in": "path",
                                "type": "string"
                            }
                        ],
                        "tags": ["tags"] 
                    },
                    "post": {
                        "responses": {
                                200: {
                                    "description": "Success"
                                }
                            },
                        "parameters": [
                            {
                                "name": "payload",
                                "required": True,
                                "in": "body",
                                "schema": {
                                    "$ref": "#/definitions/tag_model"
                                }
                            }
                        ],
                        "tags": ["tags"]                      
                    },
                },
                #"/api/history/{tag_id}": {}
            },
            "info": {
                "title": "Rackio Engine API",
                "version": "1.0",
                "description": "Rackio Engine RESTful API for system integration"
            },
            "produces": ["application/json"],
            "consumes": ["application/json"],
            "tags": [
                {
                    "name": "tags",
                    "description": "Namespace for tags"
                },
                {
                    "name": "history",
                    "description": "Namespace for history"
                }
            ],
            "definitions": {
                "tag_model": {
                    "required": ["value"],
                    "properties": {
                        "value": {
                            "type": "string",
                            "description": "String representation of tag value"
                        }
                    },
                    "type": "object"
                }
            }
        }

        return swagger

    def register_schema(self):

        def get_schema():
            return self.core_swagger()

        class SwaggerSchema:

            def on_get(self, req, resp):

                resp.body = json.dumps(get_schema(), ensure_ascii=False)

        self.app._api.add_route('/swagger/swagger.json', SwaggerSchema())

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

        self.register_schema()

    def __call__(self, app):

        self.app = app

        self.register_swagger()