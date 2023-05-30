import json

import pydirectinput
import pygetwindow
import pyautogui
import time

jue_se_count  = 2

def get_window_process():
    window_process = pygetwindow.getActiveWindow()

    title = window_process.title
    left = window_process.left
    top = window_process.top
    width = window_process.width
    height = window_process.height
    d = {
        "title :": title,
        "left  :": left,
        "top   :": top,
        "width :": width,
        "height:": height,
    }
    # print(json.dumps(d, indent=4, ))
    return  top, left, width, height


def cai_shu_ju():
    image_num = 425
    while True:
        image = pyautogui.screenshot(region=get_window_process())
        # image.save('./model_image/' + str(image_num) + '.png')

        image.save('./image/' + str(image_num) + '.png')
        image_num += 1
        time.sleep(0.5)
        print("截图", image_num, "次")


def mai_zhuang_bei():
    l = ['a', 'space', 'left', 'space', 'esc', 'f10']
    for i in l:
        pydirectinput.press(i)
        time.sleep(0.2)

def yi_jian_shi_qu():
    pydirectinput.press('0')  # 小键盘的0


# 开启被动
def kai_bei_dong():
    pydirectinput.keyDown('right')
    pydirectinput.keyUp('right')
    pydirectinput.keyDown('right')
    pydirectinput.keyUp('right')
    pydirectinput.keyDown('space')
    pydirectinput.keyUp('space')
    time.sleep(0.2)
    pydirectinput.press('t')



def pao_tu(fang_xiang, miao):
    pydirectinput.press(fang_xiang)  # 操作键盘 右键
    pydirectinput.keyDown(fang_xiang)  # 按住右键
    print("向", fang_xiang, "跑")
    time.sleep(miao)
    pydirectinput.keyUp(fang_xiang)


def stop_pao_tu():
    pydirectinput.keyUp('right')
    pydirectinput.keyUp('left')
    pydirectinput.keyUp('up')
    pydirectinput.keyUp('down')


def shu_biao_dan_ji(x,y):
    pydirectinput.moveTo(x, y)
    time.sleep(2)
    pydirectinput.mouseDown()
    time.sleep(0.1)
    pydirectinput.mouseUp()

def shu_biao_shuang_ji(x,y):
    pydirectinput.moveTo(x, y)
    time.sleep(2)
    pydirectinput.mouseDown()
    time.sleep(0.1)
    pydirectinput.mouseUp()
    time.sleep(0.1)
    pydirectinput.mouseDown()
    time.sleep(0.1)
    pydirectinput.mouseUp()


def jian_pan_cao_zuo(p,slp_time):
    pydirectinput.keyDown(p)
    time.sleep(slp_time)
    pydirectinput.keyUp(p)


def go_to_fu_ben():
    # # 走到 传送门
    jian_pan_cao_zuo('right',3)
    time.sleep(3)

    # 点击 谢拉比尔号
    shu_biao_dan_ji(500,450)
    time.sleep(3)

    # 点击传送地图
    shu_biao_dan_ji(730, 300)
    time.sleep(3)

    # 点击克洛克斯岛
    shu_biao_shuang_ji(600, 430)
    shu_biao_shuang_ji(600, 430)

    # 进入地图
    pydirectinput.keyDown('right')
    time.sleep(3)
    pydirectinput.keyUp('right')

    # 选择毁坏的寂静村
    shu_biao_shuang_ji(348, 320)
    shu_biao_shuang_ji(348, 320)

def xun_jue_se(jue_se_num):
    # 第一排角色
    # pydirectinput.moveTo(140, 230)
    # pydirectinput.moveTo(325, 260)
    # pydirectinput.moveTo(500, 260)
    # pydirectinput.moveTo(685, 250)

    # 第二排角色
    # pydirectinput.moveTo(240, 550)
    # pydirectinput.moveTo(415, 550)
    # pydirectinput.moveTo(550, 550)
    # pydirectinput.moveTo(85, 550)

    # shu_biao_shuang_ji(85, 550)
    # shu_biao_shuang_ji(240, 550)
    # shu_biao_shuang_ji(415, 550)
    # shu_biao_shuang_ji(550, 550)

    if jue_se_num == 2:
        shu_biao_shuang_ji(240, 550)
    if jue_se_num == 3:
        shu_biao_shuang_ji(415, 550)
    if jue_se_num == 4:
        shu_biao_shuang_ji(550, 550)

    print("角色选择失败")


def huan_juse_se():
    global jue_se_count
    # 回城
    jian_pan_cao_zuo('f12',0.5)
    time.sleep(3)

    # esc 选择角色
    jian_pan_cao_zuo('esc',0.5)
    shu_biao_dan_ji(480,655)
    xun_jue_se(jue_se_count)
    jue_se_count+=1


def start():
    pass

if __name__ == '__main__':
    for i in range(3,0,-1):
        print(i,"秒之后开始")
        time.sleep(1)

    # xun_jue_se()
    # kai_bei_dong()
    # huan_juse_se()
    # go_to_fu_ben()
    cai_shu_ju()
