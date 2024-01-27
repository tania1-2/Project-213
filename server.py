import socket
from  threading import Thread
from pynput.mouse import Button, Controller
from screeninfo import get_monitors
from pynput.keyboard import Key, Controller


SERVER = None
Port = 8000
IP_Adress = 162.168.0.111
screen_width = None
screen_height = None



keyboard = Controller()



def setup():
    print("\n\t\t\t\t\t''' Welcome To Remote Mouse '''\n")
    global SERVER
    global PORT
    global IP_ADDRESS