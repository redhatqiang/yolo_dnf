import time
import pydirectinput
import pyautogui


def RenOperation(direction):
    pydirectinput.keyDown(direction)
    time.sleep(0.1)
    pydirectinput.keyUp(direction)
    time.sleep(0.1)
    pydirectinput.keyDown(direction)


def StopRun():
    pydirectinput.keyUp('up')
    pydirectinput.keyUp('down')
    pydirectinput.keyUp('left')
    pydirectinput.keyUp('right')

def Operation(key):
    pydirectinput.keyDown(key)
    time.sleep(0.1)
    pydirectinput.keyUp(key)


def TypingOperation(input_str):
    pydirectinput.typewrite(input_str)


def KaiBeiDong():
    Operation('right')
    Operation('right')
    Operation('space')
    Operation('t')

def MaiZhuangBei():
    pass






if __name__ == '__main__':
    # LeftRun()
    # TopRun()
    # RightRun()
    # DownRun()
    # Operation("a")
    # TypingOperation("woshinibaba ")
    pass