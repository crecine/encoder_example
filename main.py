from macropad import Macropad

mp = Macropad()

while True:
    mp.SW.read_queue()

    event = mp.keys.events.get()
    if event:
        key_number = event.key_number
        key_command = mp.key_commands[key_number]
        if type(key_command) is not list: key_command = [key_command]

        if event.pressed:
            mp.keyboard.press(*key_command)

        if event.released:
            mp.keyboard.release(*key_command)

