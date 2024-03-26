import pyautogui
import os
import time
from PIL import Image 
import pydirectinput

def load_images_from_folder():
    folder = '.\AvoidSpin'
    images = []
    # Supported image extensions
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
    #Code finds the spin button png and clicks it on full screen (don't mess with this). If you're spin button is green, this won't work (will fix in future)
    loc = pyautogui.locateOnScreen('[Put Spin Button file path here]', confidence=0.9)
    test = pyautogui.center(loc)
    images = load_images_from_folder()
    check = True
    while check:
        pydirectinput.moveTo(test.x, test.y)
        pydirectinput.moveTo(test.x, test.y+1)
        pydirectinput.leftClick()
        time.sleep(.25)
        check = avoidCheck(images)

Spin()   
