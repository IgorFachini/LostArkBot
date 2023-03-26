import pydirectinput, pyautogui, time
from utils.general import sleep

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
    
