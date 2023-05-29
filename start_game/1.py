import json
import time

import pydirectinput
import pygetwindow
import pyautogui
# opencv  yolov8


# 打字功能  输出 hello  hello
# pydirectinput.typewrite("hello ")
# pydirectinput.typewrite(" ")
# pydirectinput.typewrite("hello ")


# 双击鼠标
# pydirectinput.doubleClick()

# 移动鼠标
# pydirectinput.moveTo(100,100)

# 单机鼠标
# pydirectinput.click()

#键盘指令
# pydirectinput.press('left')
# pydirectinput.press('left')
# pydirectinput.press('space')


# 按住某个键 比如 crtl + a
# time.sleep(3)
# pydirectinput.keyDown('ctrl')
# pydirectinput.press('a')
# pydirectinput.keyUp('ctrl')


# 开启被动
def open():
    pydirectinput.press('right')
    pydirectinput.press('rifht')
    pydirectinput.press('space')
    pydirectinput.press('t')

# 获取当前的应用 的宽高
def get_window_process():
    window_process = pygetwindow.getActiveWindow()

    title  = window_process.title
    left   = window_process.left
    top    = window_process.top
    width  = window_process.width
    height = window_process.height
    d = {
        "title :": title,
        "left  :": left,
        "top   :": top,
        "width :": width,
        "height:": height,
    }
    print(json.dumps(d,indent=4))
    return d


def sand_hand():
    pydirectinput.press('insert')  # 小键盘的0
    #pydirectinput.press('delete')  # 小键盘的.

if __name__ == '__main__':

    sleep_time = 3
    print(str(sleep_time)+ "s 之后启动 ")
    # time.sleep(sleep_time)
    #
    zuo_biao = get_window_process()
    width = zuo_biao["width :"]
    height = zuo_biao["height:"]
    print(width, height)
    print(width*0.5, height*0.5)

    pydirectinput.moveTo(int(width*0.5),int(height*0.5))
    # pydirectinput.move(500,500)
    image = pyautogui.screenshot(region=get_window_process())  # 循环截图
    # image.save('./aa.png')
    # pydirectinput.press('shift')
    # pydirectinput.moveTo(100, 100)
    # time.sleep(2)
    # pydirectinput.doubleClick()
