
import board
import usb_hid
import keypad

from adafruit_hid.keyboard import Keyboard
from adafruit_hid.consumer_control import ConsumerControl

from wombat_functions import wombat_chip, encoder
from pin_defs import key_pins
from basic_numpad import default_profile

class Macropad():
    def __init__(self):
        self.SW = wombat_chip(sda_pin=board.GP18, scl_pin=board.GP19)
        self.SW.display_details()

        self.keyboard = Keyboard(usb_hid.devices)
        self.consumer = ConsumerControl(usb_hid.devices)
        self.keys = keypad.Keys(key_pins,value_when_pressed=True,pull=True,interval=.001)
        self.key_commands = default_profile.key_commands

        self.encoder1 = self.init_knob(15,14)
        self.encoder2 = self.init_knob(17,16)
        self.encoder3 = self.init_knob(19,18)
        self.SW.flush_queue()
        
        print('Finished Setup')
        
    def init_knob(self,clk:int,dt:int):
        return encoder(self,clk,dt)

