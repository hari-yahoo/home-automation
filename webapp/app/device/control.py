from pyfirmata2 import Arduino
import json

class Controls(object):

    board = None
    config = None


    def __init__(self):
        try:
            with open('config.json', 'r') as file:
                self.config = json.load(file)

            board_port = self.config["serialPort"] # /dev/ttyACM3
        except:
            print("Failed to load or parse config.json.")
            exit()
        self.board = Arduino(board_port)
        

    def __del__(self):
        if self.board:
            self.board.exit()

