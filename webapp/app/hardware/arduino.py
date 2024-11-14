from pyfirmata2 import Arduino, OUTPUT

class ArduinoUno:
    def __init__(self, board_port):
        print("Initializing Board...")
        try:
            self.board = Arduino(board_port)
            print("Board created successfully.")
        except Exception as e:
            print(f"Error initializing board: {e}")
            self.board = None

    def get_digital_pin(self, pin_number):
        if self.board:
            return self.board.digital[pin_number]
        else:
            print("Board is not initialized.")
            return None
    
    def close(self):
        if self.board:
            self.board.exit()
            self.board = None
            print("Board connection closed.*")

    def __del__(self):
        # Fallback in case close() was not called
        self.close()
    