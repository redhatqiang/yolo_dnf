import time


def StartFirstTrainYOLOV8():
    pass

def StartSecondTrainYOLOV8():
    pass

def StartRepeatTrainYOLOV8():
    pass


if __name__ == '__main__':
    print("start yolo first train")
    StartFirstTrainYOLOV8()
    print("yolo first train success")
    time.sleep(3)

    print("start yolo second train")
    StartSecondTrainYOLOV8()
    print("yolo second train success")
    time.sleep(3)

    print("start yolo Repeat train")
    StartSecondTrainYOLOV8()
    print("yolo train success")