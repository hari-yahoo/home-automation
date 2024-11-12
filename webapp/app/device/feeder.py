from pyfirmata import SERVO
from .control import Controls
import time


class Feeder(Controls):

    position = 0
    def __init__(self, pin):
        super().__init__()
        self.pin = pin
        self.board.servo_config(self.pin)
        self.servo = self.board.digital[self.pin]
        self.servo.mode = SERVO
        
        self.servo.write(0) 

    def feed(self, duration_seconds=1):
        self.set_position(180, 0.015)
        time.sleep(duration_seconds)
        self.set_position(0, 0.015)        

        print(f"Pet fed for {duration_seconds} seconds.")
        return True
    
    def off(self):
        pass
    
    def close(self):
        if self.servo:
            self.servo.write(0)
 
    
    def set_position(self, new_position, delay=0.01):
        # move it slow, rather than setting the desired position directly
        while abs(self.position - new_position) > 0.1:
            if self.position <= new_position:
                self.position += 1.0
            elif self.position > new_position:
                self.position -= 1.0
      
            self.servo.write(self.position)
            time.sleep(delay)
        return
    

    def __del__(self):
        self.close()
        super().__del__()
