import pyautogui as pt
from time import sleep
import pyperclip
import random

sleep(3)

position1 = pt.locateOnScreen("smiley_paperclip.png", confidence=.6)
x = position1[0]
y = position1[1]

#Gets message
def get_message():
    global x, y

    position = pt.locateOnScreen("whatsapp/smiley_paperclip.png", confidence=.6)
    x = position[0]
    y = position[1]
    pt.moveTo(x, y, duration=.05)

get_message()