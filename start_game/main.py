from start_game.next_person import NextPerson
from start_game.next_game import NextGame
from start_game.keyboard_operation import LeftRun,TopRun,RightRun,DownRun,StopRun,KaiBeiDong
import win32gui
import win32ui
import win32con
import numpy
import cv2
import pygetwindow
import time

class StartGame():
    def __int__(self):
        self.bei_dong = False

    def next_game(self):
        NextGame()
        self.__int__()

    def next_person(self):
        NextPerson()
        self.__int__()

    def kai_bei_dong(self):
        if not self.bei_dong:
            KaiBeiDong()
            self.bei_dong = True


    def start(self):
        count = 0
        print("start load yolo model")
        print("load model success ")

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
        print("get windows app process info : ", d)

        for i in range(3, 0, -1):
            print(i, "s after start ")
            time.sleep(1)

        print("start run ")
        time.sleep(1)

        while True:
            hdesktop = win32gui.GetDesktopWindow()
            desktop_dc = win32gui.GetWindowDC(hdesktop)
            img_dc = win32ui.CreateDCFromHandle(desktop_dc)
            mem_dc = img_dc.CreateCompatibleDC()
            screenshot = win32ui.CreateBitmap()
            screenshot.CreateCompatibleBitmap(img_dc, width, height)
            mem_dc.SelectObject(screenshot)
            mem_dc.BitBlt((0, 0), (width, height), img_dc, (left, top), win32con.SRCCOPY)

            # 展示图片 使用 numpy 转换
            signedIntsArray = screenshot.GetBitmapBits(True)
            img = numpy.frombuffer(signedIntsArray, dtype='uint8')
            img.shape = (height, width, 4)

            # 使用opencv 显示到屏幕
            # cv2.cvtColor(img, cv2.COLOR_BGRA2RGB)
            # cv2.imwrite("img.jpg",img,[int(cv2.IMWRITE_JPEG_QUALITY), 100])
            # cv2.namedWindow('img')
            cv2.imshow("img", img)
            cv2.waitKey(1)

            # 保存图片到本地
            # screenshot.SaveBitmapFile(mem_dc, 'screenshot.png')

            # 释放临时内存
            mem_dc.DeleteDC()
            win32gui.DeleteObject(screenshot.GetHandle())

            # count += 1
            # print("截图了", count, "次")
            # time.sleep(1)
            # return




if __name__ == '__main__':
    app = StartGame()
    app.start()

