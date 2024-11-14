import json
import RPi.GPIO as GPIO

class Controller(object):

    def __init__(self):
        self.load_config()

    def load_config(self):
        try:
            with open('config.json', 'r') as file:
                self.config = json.load(file)
        except FileNotFoundError:
            print("Config file not found.")
    
    def turn_off_relay_power(self):
        print("Turning off relay power")
        pin = self.config["RelayPowerPin"]
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, GPIO.LOW)
        GPIO.cleanup()
    
    def turn_on_relay_power(self):
        print("Turning on relay power")
        pin = self.config["RelayPowerPin"]
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, GPIO.HIGH)
        GPIO.cleanup()