from adafruit_hid.keycode import Keycode
from adafruit_hid.consumer_control_code import ConsumerControlCode
import displayio
import time

class basic_modules():
    Keycode = Keycode
    ConsumerControlCode = ConsumerControlCode
    displayio = displayio
    time = time

class default_profile():        
    key_commands = (
        basic_modules.Keycode.KEYPAD_ZERO,
        basic_modules.Keycode.KEYPAD_ONE,
        basic_modules.Keycode.KEYPAD_TWO,
        basic_modules.Keycode.KEYPAD_THREE,
        basic_modules.Keycode.KEYPAD_FOUR,
        basic_modules.Keycode.KEYPAD_FIVE,
        basic_modules.Keycode.KEYPAD_SIX,
        basic_modules.Keycode.KEYPAD_SEVEN,
        basic_modules.Keycode.KEYPAD_EIGHT,
        basic_modules.Keycode.KEYPAD_NINE,
        basic_modules.Keycode.KEYPAD_NUMLOCK,
        basic_modules.Keycode.KEYPAD_FORWARD_SLASH,
        basic_modules.Keycode.KEYPAD_ASTERISK,
        basic_modules.Keycode.KEYPAD_MINUS,
        basic_modules.Keycode.KEYPAD_PLUS,
        basic_modules.Keycode.KEYPAD_ENTER,
        basic_modules.Keycode.KEYPAD_PERIOD,
    )

    @staticmethod
    def encoder2_commands(mp):
        direction = mp.encoder2.direction
        if direction == 1:
            mp.consumer.send(basic_modules.ConsumerControlCode.VOLUME_INCREMENT)
        elif direction == -1:
            mp.consumer.send(basic_modules.ConsumerControlCode.VOLUME_DECREMENT)

    @staticmethod
    def encoder3_commands(mp):
        direction = mp.encoder3.direction
        mp.keyboard.press(basic_modules.Keycode.ALT)
        print('press')
        ii=0
        while ii < 9 :
            if direction == 1:
                ii=0
                mp.keyboard.press(basic_modules.Keycode.TAB)
                time.sleep(.001)
                mp.keyboard.release(basic_modules.Keycode.TAB)
            elif direction == -1:
                ii=0
                mp.keyboard.press(basic_modules.Keycode.TAB,basic_modules.Keycode.SHIFT)
                time.sleep(.001)
                mp.keyboard.release(basic_modules.Keycode.TAB,basic_modules.Keycode.SHIFT)
            ii+=1
            time.sleep(.1)
            val3, direction = mp.encoder3.update()
        mp.keyboard.release(basic_modules.Keycode.ALT)
        print('release')

profile = default_profile
