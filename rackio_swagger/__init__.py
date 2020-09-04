# rackio_swagger/__init__.py

from .core import SwaggerCore
from .schema import SchemaManager

RackioSwagger = SwaggerCore()
SwaggerManager = SchemaManager()