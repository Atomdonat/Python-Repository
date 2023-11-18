import pyautogui
import time

def write(text:str):
    time.sleep(10) # delay to enter target window

    for char in text:
        pyautogui.press(char) # 'paste' text 'manually'

## Purpose:
# Copy and paste text into the terminal where there is no clipboard, 
