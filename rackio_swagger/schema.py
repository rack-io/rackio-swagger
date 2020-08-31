# -*- coding: utf-8 -*-
"""rackio_swagger/schema.py

This module implements the schema dict to produce the json schema.
"""

def get_schema():

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
                            "name": "tag_id",
                            "required": True,
                            "in": "path",
                            "type": "string"
                        },
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
            "/history/{tag_id}": {
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
                    "tags": ["history"]
                },
            },
            "/trends": {
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
                                "$ref": "#/definitions/trend_model"
                            }
                        }
                    ],
                    "tags": ["trends"]
                }
            },
            "/trends/{tag_id}": {
                "parameters": [
                    {
                        "name": "tag_id",
                        "required": True,
                        "in": "path",
                        "type": "string"
                    }
                ],
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
                                "$ref": "#/definitions/trend_model"
                            }
                        }
                    ],
                    "tags": ["trends"]
                },
                "/controls": {

                },
                "/controls/{control_name}": {

                },
                "/rules": {

                },
                "/rules/{rule_name}": {

                },
                "/alarms": {

                },
                "/alarms/{alarm_name}": {

                },
                "/events": {

                },
                "/summary": {

                }
            },
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
                "description": "Namespace for tag history"
            },
            {
                "name": "trends",
                "description": "Namespace for tag trends"
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
            },
            "trend_model": {
                "required": ["tags", "tstart", "tstop"],
                "properties": {
                    "tags": {
                        "type": "array",
                        "items": {
                            "type": "string"
                        },
                        "description": "List of Strings representing tag names"
                    },
                    "tstart": {
                        "type": "string",
                        "description": "Start time for trend (format: %Y-%m-%d %H:%M:%S)"
                    },
                    "tstop": {
                        "type": "string",
                        "description": "Start time for trend (format: %Y-%m-%d %H:%M:%S)"
                    },
                },
                "type": "object"
            }
        }
    }

    return swagger