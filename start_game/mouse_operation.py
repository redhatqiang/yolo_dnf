import time
import pydirectinput
import pyautogui

def MouseClick(x,y):
    pydirectinput.moveTo(x,y)
    time.sleep(1)
    pydirectinput.click()

def MouseDoubleClick(x,y):
    pydirectinput.moveTo(x, y)
    time.sleep(1)
    pydirectinput.click()
    time.sleep(0.1)
    pydirectinput.click()


if __name__ == '__main__':
    # MouseClick(996,438)
    # MouseDoubleClick(996,438)

    pass