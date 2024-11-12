from pyfirmata2 import SERVO, OUTPUT
from .control import Controls



class Light(Controls):
    device = None
    pin = 0

    def __init__(self, pin=10):
        super().__init__()
        self.pin = pin
        print(pin)
        #self.device = self.board.get_pin('d ' + str(self.pin) + ' o')    
        self.device = self.board.digital[self.pin]
        self.device.mode = OUTPUT
        

    def on(self):
        self.device.write(True)


    def off(self):
        self.device.write(False)

    def __del__(self):
        super().__del__()
