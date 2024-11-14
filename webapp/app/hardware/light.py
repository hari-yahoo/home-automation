
from pyfirmata2 import SERVO, OUTPUT


class Light(object):
    device = None
    pin = 0

    def __init__(self, arduino, pin=10):
        super().__init__()
        self.pin = pin
        self.board = arduino   
        self.device = self.board.get_digital_pin(pin)
        if self.device is not None:
            self.device.mode = OUTPUT
            self.off()
            print(f"Digital pin {pin} initialized")
        else:
            print(f"Failed to initialize digital pin {pin}")
       
    def on(self):
        if self.device is not None:
            self.device.write(0)  # Assuming active-low relay
            self.is_on = True
            print("Light turned on.")
        else:
            print("Device not initialized. Cannot turn on the light.")

    def off(self):
        if self.device is not None:
            self.device.write(1)  # Assuming active-low relay
            self.is_on = False
            print("Light turned off.")
        else:
            print("Device not initialized. Cannot turn off the light.")
    
    def __del__(self):
        print("Light object is being deleted.")
