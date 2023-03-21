import pyautogui
import pydirectinput
import utils.game as utilsGame
from utils.general import mouseMoveTo, sleep

# while True:
# print(pyautogui.displayMousePosition())
pydirectinput.keyDown("alt")
pydirectinput.press("q")
pydirectinput.keyUp("alt")


chaosDungeonIcon = pyautogui.locateCenterOnScreen(
                "./screenshots/chaosDungeonDisableIcon.png",
                confidence=0.60
            )

shortcutIcon = pyautogui.locateCenterOnScreen(
                "./screenshots/shortcutIcon.png",
                confidence=0.60,
                region=(chaosDungeonIcon.x -10, chaosDungeonIcon.y -10, 595, 83)
            )
pydirectinput.click(shortcutIcon.x, shortcutIcon.y)


c1 = pyautogui.locateCenterOnScreen(
                "./screenshots/northVernChaosDungeonLabelUnselected.png",
                confidence=0.60
            )
pydirectinput.click(c1.x, c1.y)
c2 = pyautogui.locateCenterOnScreen(
                "./screenshots/rohendelChaosDungeonLabelUnselected.png",
                confidence=0.60
            )
pydirectinput.click(c2.x, c2.y)

c3 = pyautogui.locateCenterOnScreen(
                "./screenshots/yornChaosDungeonLabelUnselected.png",
                confidence=0.60
            )
pydirectinput.click(c3.x, c3.y)

c4 = pyautogui.locateCenterOnScreen(
                "./screenshots/feitonChaosDungeonLabelUnselected.png",
                confidence=0.60
            )
pydirectinput.click(c4.x, c4.y)

c5 = pyautogui.locateCenterOnScreen(
                "./screenshots/punikaChaosDungeonLabelUnselected.png",
                confidence=0.60
            )
pydirectinput.click(c5.x, c5.y)

c6 = pyautogui.locateCenterOnScreen(
                "./screenshots/southVernChaosDungeonLabelUnselected.png",
                confidence=0.60
            )
pydirectinput.click(c6.x, c6.y)

# -10 locateCenterOnScreen shortcutIcon
# 1920x1080 - 2560x1080 133
# x + 595  y 83