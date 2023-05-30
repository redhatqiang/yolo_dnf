import time
import pydirectinput
import pyautogui


def LeftRun():
    pydirectinput.keyDown('left')


def RightRun():
    pydirectinput.keyDown('right')


def TopRun():
    pydirectinput.keyDown('up')


def DownRun():
    pydirectinput.keyDown('down')


def StopRun():
    pydirectinput.keyUp('up')
    pydirectinput.keyUp('down')
    pydirectinput.keyUp('left')
    pydirectinput.keyUp('right')


def Operation(key):
    pyautogui.keyDown(key)
    # pydirectinput.keyDown(key)
    time.sleep(0.2)
    pyautogui.keyUp(key)
    # pydirectinput.keyUp(key)

def TypingOperation(input_str):
    pydirectinput.typewrite(input_str)

def KaiBeiDong():
    Operation('right')
    Operation('right')
    Operation('space')




if __name__ == '__main__':
    # LeftRun()
    # TopRun()
    # RightRun()
    # DownRun()
    # Operation("a")
    # TypingOperation("woshinibaba ")
    pass