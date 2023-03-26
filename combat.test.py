from abilities import abilities
from utils.game import checkCDandCast
import pyautogui, time
from screeninfo import get_monitors

while True:
    for i in range(0, 8):
        print(i)
        abilities["deathblade"][i] = checkCDandCast(abilities["deathblade"][i])
