import time

from random import random

from rackio import Rackio, TagEngine
from rackio_swagger import RackioSwagger

app = Rackio()

RackioSwagger(app)

tag_egine = TagEngine()

# Tags definitions

tag_egine.set_tag("T1", "float")
tag_egine.set_tag("T2", "float")
tag_egine.set_tag("T3", "float")

@app.rackit(1)
def writer1():

    tag_egine.write_tag("T1", 15)
    tag_egine.write_tag("T2", 40)

    direction = 1

    while True:

        time.sleep(0.5)

        T1 = tag_egine.read_tag("T1")
        T1 += direction

        tag_egine.write_tag("T1", T1)

        if T1 >= 60:
            direction *= -1

        if T1 <= 5:
            direction *= -1

if __name__ == "__main__":

    app.run(8030)