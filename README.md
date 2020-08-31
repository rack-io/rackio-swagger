# rackio-swagger
A Rackio extension to enable Swagger UI in API definitions

## Installation

```
pip install RackioSwagger
```

## Usage

```python
from rackio import Rackio
from rackio_swagger import RackioSwagger

app = Rackio()

RackioSwagger(app)

app.run(8028)
```

## Swagger UI

After running your application you will find the UI in the following address.

```
http://localhost:8028/swagger
```

