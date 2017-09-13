from gopigo import *

#############MY CLASS
class Piggy(object):
    def_int_(self):

        print("Hello, I am your robot")
        self.dance()

    def dance(self):
        fwd()
        time.sleep(1.5)
        right_rot()
        time.sleep(.5)
        stop()

##### MY APP
mra = Piggy()