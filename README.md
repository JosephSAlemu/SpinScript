# SpinScript
A video game didn't have a feature to prevent users from spinning off rare stuff, so I made something simple to help with that

# What to install (Windows)
- Install Python 3.8
  > Any Python version that supports Pillow
- Make sure pip is up to date
  > python -m pip install --upgrade pip
- Install OpenCV
  > pip install opencv-python
- Install Pyautogui
  > pip install pyautogui
- Install Pydirectinput
  > pip install pydirectinput
- Install Keyboard
  > pip install keyboard
- VScode or your favorite text editor
  > preferably NeoVim

# How to use
-Make sure your game instance is maximized.

-Take a photo of the spin button and put the file path in the spin function as indicated

-Screenshot the spin stuff you want and put it in a file for the WantSpins script. Then set the file path to it.

-Screenshot what you don't want and put it in a file for the AvoidSpins script. Then set the file path to it.

-Press esc key to end the script

# Important
- Pyautogui is not perfect at detecting images on the screen, so test the script before going for something rare
- Just whipped this up in a few hours (most spent figuring out how to install Python)
- Make sure to adjust the confidence interval if Pyautogui isn't detecting images.
 
