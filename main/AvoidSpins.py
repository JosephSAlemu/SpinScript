import pyautogui
import os
import time
import pydirectinput
import keyboard
import threading

def load_images_from_folder():
    folder = '[Images Folder/Directory]'
    images = []
    #Supported image extensions
    valid_extensions = [".jpg", ".jpeg", ".png", ".gif", ".bmp"]
    #Just getting every image from the File Path I specify
    for filename in os.listdir(folder):
        if any(filename.lower().endswith(ext) for ext in valid_extensions):
            img_path = os.path.join(folder, filename)
            images.append(img_path)
    return images

def avoidCheck(images):
    common = False
    for image in images:
        try:
            #Mess with the confidence on this if you want to change how accurate the script is detecting images (Do this if you're having detection issues).
            pyautogui.locateOnScreen(image, confidence=0.8)
            common = True
            #Just logging any matches that happen
            print('Match at' + image)
        except:
            pass
    return common

def Spin():
    def stop():
        event.set()
        print("Script Ended")
    #Threading so I can close the thread with the esc key
    event = threading.Event()
    keyboard.add_hotkey("esc", stop)
    #Code finds the spin button png and clicks it on full screen (don't mess with this). If you're spin button is green, this won't work (will fix in future)
    loc = pyautogui.locateOnScreen('[Spin Button png]', confidence=0.9)
    test = pyautogui.center(loc)
    images = load_images_from_folder()
    check = True
    while check and not event.is_set():
        pydirectinput.moveTo(test.x, test.y)
        pydirectinput.moveTo(test.x, test.y+1)
        pydirectinput.leftClick()
        check = avoidCheck(images)

Spin()
