import json
import RPi.GPIO as GPIO

class Controller(object):

    def __init__(self):
        
        self.load_config()
        self.relay_power_pin = self.config["RelayPowerPin"]
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.relay_power_pin, GPIO.OUT)

    def load_config(self):
        try:
            with open('config.json', 'r') as file:
                self.config = json.load(file)
        except FileNotFoundError:
            print("Config file not found.")
    
    def turn_off_relay_power(self):
        print("Turning off relay power")
        GPIO.output(self.relay_power_pin, GPIO.LOW)
       
    
    def turn_on_relay_power(self):
        print("Turning on relay power")
        GPIO.output(self.relay_power_pin, GPIO.HIGH)
