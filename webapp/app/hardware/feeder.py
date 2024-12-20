
from pyfirmata2 import SERVO

import time


class Feeder(object):

    
    def __init__(self, arduino, pin):
        
        self.servo = None
        self.position = 0
        self.board = arduino
        self.pin = pin
        
        self.board.servo_config(self.pin)
        self.servo = self.board.get_digital_pin(pin)
        if self.servo is not None:
            self.servo.mode = SERVO
            self.servo.write(0)
            print(f"Digital pin {pin} initialized")
        else:
            print(f"Failed to initialize digital pin {pin}")
       
    def feed_fast(self, duration=1, angle=90):
        if self.servo is not None:
            self.servo.write(angle)
            time.sleep(duration)
            self.servo.write(0)
            return True
        else:
            print(f"Failed to start feeding")
            return False


    def feed(self, duration_seconds=1):
        if self.servo is not None:
            self.set_position(180, 0.015)
            time.sleep(duration_seconds)
            self.set_position(0, 0.015)        

            print(f"Pet fed for {duration_seconds} seconds.")
            return True
        else:
            print(f"Failed to start feeding")
            return False
    
    def off(self):
        pass
    
    def close(self):
        if self.servo:
            self.servo.write(0)
 
    
    def _set_position(self, new_position, delay=0.01):
        # move it slow, rather than setting the desired position directly
        while abs(self.position - new_position) > 0.1:
            if self.position <= new_position:
                self.position += 1.0
            elif self.position > new_position:
                self.position -= 1.0
      
            self.servo.write(self.position)
            time.sleep(delay)
        return
    
    def set_position(self, new_position, increment=1.0, delay=0.01):
        # move it slow, rather than setting the desired position directly
        while abs(self.position - new_position) > 0.1:
            if self.position <= new_position:
                self.position += increment
            elif self.position > new_position:
                self.position -= increment
      
            self.servo.write(self.position)
            time.sleep(delay)
        return
    

    def __del__(self):
        self.close()
      
