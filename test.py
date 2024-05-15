import pyautogui
import time

def write(text:str):
    time.sleep(5)

    for char in text:
        pyautogui.press(char)


write("ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIOuDafOZSpKnrNN1ncacH0GqlOpnLe3gyJ6tyDgIVbBe buste@Flex5i")

# Primitive virtual keyboard emulator to paste text in target window. When copy and past doesn't work, for example in web consoles:
# - enter text to be pasted in write("")
# - run program
# - switch to target window
# - wait until its done