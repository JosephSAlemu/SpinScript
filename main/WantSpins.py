import pyautogui
import os
import time
import pydirectinput

def load_images_from_folder():
    folder = '[Put Directory With Images Of Desired Spins Here]'
    images = []
    #Supported image extensions
    valid_extensions = [".jpg", ".jpeg", ".png", ".gif", ".bmp"]
    #Just getting every image from the File Path I specify
    for filename in os.listdir(folder):
        if any(filename.lower().endswith(ext) for ext in valid_extensions):
            img_path = os.path.join(folder, filename)
            images.append(img_path)
    return images

def wantCheck(images):
    common = True
    for image in images:
        print(image)
        try:
            #Mess with the confidence on this if you want to change how accurate the script is detecting images (Do this if you're having detection issues).
            pyautogui.locateOnScreen(image, confidence=0.8)
            common = False
            #Just logging any matches that happen
            print('Match at' + image)
        except:
            pass
    return common

def Spin():
    #Code finds the spin button png and clicks it on full screen
    loc = pyautogui.locateOnScreen('[Put Spin Button File Path Here]', confidence=0.9)
    test = pyautogui.center(loc)
    images = load_images_from_folder()
    check = True
    while check:
        #Positions mouse to spin button
        pydirectinput.moveTo(test.x, test.y)
        #Game doesn't like when you instantly teleport your cursor for some reason, shifting it slightly to have it re-register your mouse so you can auto click.
        pydirectinput.moveTo(test.x, test.y+1)
        pydirectinput.leftClick()
        #Making the program sleep so things aren't spinned before being recognized images.
        time.sleep(.25)
        check = wantCheck(images)

Spin()   

