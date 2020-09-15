from mainUI import Pilot
from threading import Thread
import mqtt.subscriber as subscriber
from time import sleep


def num():
    root = Pilot()
    thread = Thread(target = subscriber.run, args = (root.rooms, ))
    thread.start()

    root.mainloop()
#waiting for subscriber to initialize

