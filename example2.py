import time

from random import random

from rackio import Rackio, TagEngine
from rackio_swagger import RackioSwagger
from rackio.managers import VISITOR_ROLE

app = Rackio()

RackioSwagger(app)

tag_egine = TagEngine()

# Tags definitions

tag_egine.set_tag("T1", "float")
tag_egine.set_tag("T2", "float")
tag_egine.set_tag("T3", "float")

tag_egine.set_tag("RAND1", "float")
tag_egine.set_tag("RAND2", "float")

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
        
app.define_user("Luke", "skywalker", VISITOR_ROLE)
app.define_user("rackio", "12345678", "System")


if __name__ == "__main__":

    app.set_db(dbfile="tags.db")
    app.set_log(file="app.log")
    app.set_dbtags(["RAND1", "RAND2"], 0.2)
    app.set_dbtags(["T1", "T2", "T3"], 0.5)

    app.enable_auth()
    app.run(8030)