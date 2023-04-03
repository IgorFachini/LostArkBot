import pydirectinput, pyautogui, time
from utils.general import sleep
from config import chaosDungeonPowerImagesMap

def checkCDandCast(ability):
    # if ability["directional"] == True:
    #     mouseMoveTo(x=states["moveToX"], y=states["moveToY"])
    # else:
    #     mouseMoveTo(x=config["screenCenterX"], y=config["screenCenterY"])
    sleep(50, 60)
    now_ms = int(time.time_ns() / 1000000)
    hasTimeLastCasted = "timeLastCasted" in ability
    if hasTimeLastCasted == False or now_ms - ability["timeLastCasted"] > ability["cdw"]:
        if ability["cast"]:
            start_ms = int(time.time_ns() / 1000000)
            now_ms = int(time.time_ns() / 1000000)
            while now_ms - start_ms < ability["castTime"]:
                pydirectinput.press(ability["key"])
                sleep(50, 60)
                now_ms = int(time.time_ns() / 1000000)
        elif ability["hold"]:
            pydirectinput.keyDown(ability["key"])

            time.sleep(ability["holdTime"]/1000)

            pydirectinput.keyUp(ability["key"])
        else:
            # ability
            pydirectinput.press(ability["key"])
        ability["timeLastCasted"] = int(time.time_ns() / 1000000)
        time.sleep(1)
    else:
        print('cdw')
        pydirectinput.click(button='right')
        time.sleep(0.5)
    return ability
    
# Get City And Level Path Images Object By Power, find in chaosDungeonPowerImagesMap
# @param {Number} power
# @return {Object} {cityPathImage, levelPathImage}
def getCityAndLevelPathImagesByPower(power):
    for city, cityData in chaosDungeonPowerImagesMap.items():
        for level, levelData in cityData["levels"].items():
            if levelData["power"] == power:
                return {
                    "cityPathImage": cityData["imagePath"],
                    "levelPathImage": levelData["imagePath"]
                }
    return None

# Function to Locate Center On Screen and Click By Power, use getCityAndLevelPathImagesByPower to get cityPathImage and levelPathImage
# @param {Number} power
def locateCenterOnScreenAndClickByPowerChaosDungeon(power):
    images = getCityAndLevelPathImagesByPower(power)
    if images == None:
        return None
    cityPathImage = images["cityPathImage"]
    levelPathImage = images["levelPathImage"]
    cityPath = pyautogui.locateCenterOnScreen(
        cityPathImage,
        confidence=0.70
    )
    pydirectinput.click(cityPath.x, cityPath.y)
    time.sleep(0.5)
    levelPath = pyautogui.locateCenterOnScreen(
        levelPathImage,
        confidence=0.96
    )
    pydirectinput.click(levelPath.x, levelPath.y)
    return levelPath

# Open Chaos Dungeon and select level power
# @param {Number} power
def openChaosDungeonAndSelectLevelByPower(power):
    # Open Chaos Dungeon
    pydirectinput.keyDown("alt")
    pydirectinput.press("q")
    pydirectinput.keyUp("alt")
    time.sleep(1)
    # Select Level
    locateCenterOnScreenAndClickByPowerChaosDungeon(power)


