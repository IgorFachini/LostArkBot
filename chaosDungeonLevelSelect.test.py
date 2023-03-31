import pyautogui
import pydirectinput
import utils.game as utilsGame
# while True:
# print(pyautogui.displayMousePosition())
# pydirectinput.keyDown("alt")
# pydirectinput.press("q")
# pydirectinput.keyUp("alt")


level1 = pyautogui.locateCenterOnScreen(
                "./screenshots/chaosDungeon/level1.png"
            )
pydirectinput.click(level1.x, level1.y)

level2 = pyautogui.locateCenterOnScreen(
                "./screenshots/chaosDungeon/level2.png"
            )
pydirectinput.click(level2.x, level2.y)

level3 = pyautogui.locateCenterOnScreen(
                "./screenshots/chaosDungeon/level3.png"
            )
pydirectinput.click(level3.x, level3.y)

level4 = pyautogui.locateCenterOnScreen(
                "./screenshots/chaosDungeon/level4.png"
            )
pydirectinput.click(level4.x, level4.y)



# level1Star = pyautogui.locateCenterOnScreen(
#                 "./screenshots/chaosDungeon/level1Star.png",
#                 confidence=0.90
#             )
# pydirectinput.click(level1Star.x, level1Star.y)

# level2Star = pyautogui.locateCenterOnScreen(
#                 "./screenshots/chaosDungeon/level2Star.png",
#                 confidence=0.90
#             )
# pydirectinput.click(level2Star.x, level2Star.y)

# level1Moon = pyautogui.locateCenterOnScreen(
#                 "./screenshots/chaosDungeon/level1Moon.png",
#                 confidence=0.90
#             )
# pydirectinput.click(level1Moon.x, level1Moon.y)

# level2Moon = pyautogui.locateCenterOnScreen(
#                 "./screenshots/chaosDungeon/level2Moon.png",
#                 confidence=0.90
#             )
# pydirectinput.click(level2Moon.x, level2Moon.y)

# level3Moon = pyautogui.locateCenterOnScreen(
#                 "./screenshots/chaosDungeon/level3Moon.png"
#             )
# pydirectinput.click(level3Moon.x, level3Moon.y)

# level1Sun = pyautogui.locateCenterOnScreen(
#                 "./screenshots/chaosDungeon/level1Sun.png",
#                 confidence=0.90
#             )
# pydirectinput.click(level1Sun.x, level1Sun.y)

# level2Sun = pyautogui.locateCenterOnScreen(
#                 "./screenshots/chaosDungeon/level2Sun.png",
#                 confidence=0.90
#             )
# pydirectinput.click(level2Sun.x, level2Sun.y)

# level3Sun = pyautogui.locateCenterOnScreen(
#                 "./screenshots/chaosDungeon/level3Sun.png"
#             )
# pydirectinput.click(level3Sun.x, level3Sun.y)

# chaosDungeonIcon = pyautogui.locateCenterOnScreen(
#                 "./screenshots/chaosDungeonDisableIcon.png",
#                 confidence=0.60
#             )

# shortcutIcon = pyautogui.locateCenterOnScreen(
#                 "./screenshots/shortcutIcon.png",
#                 confidence=0.60,
#                 region=(chaosDungeonIcon.x -10, chaosDungeonIcon.y -10, 595, 83)
#             )
# pydirectinput.click(shortcutIcon.x, shortcutIcon.y)


# c1 = pyautogui.locateCenterOnScreen(
#                 "./screenshots/northVernChaosDungeonLabelUnselected.png",
#                 confidence=0.60
#             )
# pydirectinput.click(c1.x, c1.y)
# c2 = pyautogui.locateCenterOnScreen(
#                 "./screenshots/rohendelChaosDungeonLabelUnselected.png",
#                 confidence=0.60
#             )
# pydirectinput.click(c2.x, c2.y)

# c3 = pyautogui.locateCenterOnScreen(
#                 "./screenshots/yornChaosDungeonLabelUnselected.png",
#                 confidence=0.60
#             )
# pydirectinput.click(c3.x, c3.y)

# c4 = pyautogui.locateCenterOnScreen(
#                 "./screenshots/feitonChaosDungeonLabelUnselected.png",
#                 confidence=0.60
#             )
# pydirectinput.click(c4.x, c4.y)

# c5 = pyautogui.locateCenterOnScreen(
#                 "./screenshots/punikaChaosDungeonLabelUnselected.png",
#                 confidence=0.60
#             )
# pydirectinput.click(c5.x, c5.y)

# c6 = pyautogui.locateCenterOnScreen(
#                 "./screenshots/southVernChaosDungeonLabelUnselected.png",
#                 confidence=0.60
#             )
# pydirectinput.click(c6.x, c6.y)

# -10 locateCenterOnScreen shortcutIcon
# 1920x1080 - 2560x1080 133
# x + 595  y 83