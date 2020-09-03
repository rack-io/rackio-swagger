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
                }
            },
            "/controls": {
                "get": {
                    "responses": {
                        200: {
                            "description": "Success"
                        }
                    },
                    "tags": ["controls"]
                }
            },
            "/controls/{control_name}": {
                "get": {
                    "responses": {
                        200: {
                            "description": "Success"
                        }
                    },
                    "parameters": [
                        {
                            "name": "control_name",
                            "required": True,
                            "in": "path",
                            "type": "string"
                        }
                    ],
                    "tags": ["controls"] 
                }
            },
            "/rules": {
                "get": {
                    "responses": {
                        200: {
                            "description": "Success"
                        }
                    },
                    "tags": ["controls"]
                }
            },
            "/rules/{rule_name}": {
                "get": {
                    "responses": {
                        200: {
                            "description": "Success"
                        }
                    },
                    "parameters": [
                        {
                            "name": "rule_name",
                            "required": True,
                            "in": "path",
                            "type": "string"
                        }
                    ],
                    "tags": ["controls"] 
                }
            },
            "/alarms": {
                "get": {
                    "responses": {
                        200: {
                            "description": "Success"
                        }
                    },
                    "tags": ["alarms"]
                }
            },
            "/alarms/{alarm_name}": {
                "get": {
                    "responses": {
                        200: {
                            "description": "Success"
                        }
                    },
                    "parameters": [
                        {
                            "name": "alarm_name",
                            "required": True,
                            "in": "path",
                            "type": "string"
                        }
                    ],
                    "tags": ["alarms"] 
                },
                "post": {
                    "responses": {
                            200: {
                                "description": "Success"
                            }
                        },
                    "parameters": [
                        {
                            "name": "alarm_name",
                            "required": True,
                            "in": "path",
                            "type": "string"
                        },
                        {
                            "name": "payload",
                            "required": True,
                            "in": "body",
                            "schema": {
                                "$ref": "#/definitions/alarm_model"
                            }
                        }
                    ],
                    "tags": ["alarms"]
                }
            },
            "/events": {
                "get": {
                    "responses": {
                        200: {
                            "description": "Success"
                        }
                    },
                    "tags": ["events"]
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
                                "$ref": "#/definitions/event_model"
                            }
                        }
                    ],
                    "tags": ["events"]
                }
            },
            "/blobs": {
                "post": {
                    "responses": {
                        201: {
                            "description": "Success"
                        }
                    },
                    "consumes": "multipart/form-data",
                    "parameters": [
                        {
                            "in": "formData",
                            "name": "name",
                            "type": "string",
                            "required": True
                        },
                        {
                            "in": "formData",
                            "name": "file",
                            "type": "file",
                            "required": True
                        }
                    ],
                    "tags": ["blobs"]
                }
            },
            "/summary": {

            }
        },
        "info": {
            "title": "Rackio Engine API",
            "version": "1.0",
            "description": "Rackio Engine RESTful API for system integration"
        },
        "produces": ["application/json"],
        "consumes": ["application/json", "multipart/form-data"],
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
            },
            {
                "name": "controls",
                "description": "Namespace for controls"
            },
            {
                "name": "alarms",
                "description": "Namespace for alarms"
            },
            {
                "name": "events",
                "description": "Namespace for events"
            },
            {
                "name": "blobs",
                "description": "Namespace for blobs"
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
            },
            "alarm_model": {
                "required": ["action"],
                "properties": {
                    "action": {
                        "type": "string",
                        "description": "Action to perform on Alarm 'Acknowledge', 'Disable', 'Enable' or 'Reset'."
                    }
                },
                "type": "object"
            },
            "event_model": {
                "required": ["user", "message", "description", "priority"],
                "properties": {
                    "user": {
                        "type": "string",
                        "description": "Username logging the event"
                    },
                    "message": {
                        "type": "string",
                        "description": "Event short message"
                    },
                    "description": {
                        "type": "string",
                        "description": "Event description"
                    },
                    "priority": {
                        "type": "integer",
                        "description": "Event priority"
                    },
                },
                "type": "object"
            }
        }
    }

    return swagger