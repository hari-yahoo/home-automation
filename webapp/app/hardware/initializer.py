import json

from .arduino import ArduinoUno
from .light import Light
from .controller import Controller

class Initializer(object):

    arduino = None

    def __init__(self):
        self.board = None
        self.config = None
        self.load_config()
       

    def load_config(self):
        try:
            with open('config.json', 'r') as file:
                self.config = json.load(file)
        except FileNotFoundError:
            print("Config file not found.")
           
    
    def initialize_board(self):
        board_port = self.config["serialPort"]

        controller = Controller()

        # disconnect power to relay coils
        controller.turn_off_relay_power()
        Initializer.arduino = ArduinoUno(board_port)
        for i in range(8):
            light = Light(Initializer.arduino, i + 6)
            light.off()

        # connect back the power
        controller.turn_on_relay_power()
        return (Initializer.arduino != None)
    
