import time
import os
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"
from ultralytics import YOLO





def StartRepeatTrainYOLOV8():

    data = "./train_dnf.yaml"
    device= "0"
    cache = True
    workers = 4
    batch = 20

    # print("train start first train ")
    # model = 'yolov8n.pt'
    # args = dict(model=model,data=data,device=device,cache=cache,workers=workers,batch=batch) # batch=16  加大这个参数提升gpu使用率
    # YOLO(model).train(**args)
    # print(" first train success")

    # for i in range(5, 0, -1):
    #     print(i, "s after start next train")
    #     time.sleep(1)

    # print("start second train")
    # model = './runs/detect/train/weights/best.pt'
    # args = dict(model=model,data=data,device=device,cache=cache,workers=workers,batch=batch) # batch=16  加大这个参数提升gpu使用率
    # YOLO(model).train(**args)
    # print("second train success")
    #
    # for i in range(5, 0, -1):
    #     print(i, "s after start next train")
    #     time.sleep(1)

    for num in range(4, 6):
        print("start ", num + 1 ,"train")
        model = './runs/detect/train' + str(num) + '/weights/best.pt'
        if not os.path.isfile(model):
            continue
        YOLO(model).train(model=model,data=data,device=device,cache=cache,workers=workers,batch=batch)
        print( num + 1, "train success")

        for i in range(5, 0, -1):
            print(i, "s after start next train")
            time.sleep(1)



if __name__ == '__main__':


    print("start yolo Repeat train")
    StartRepeatTrainYOLOV8()
    print("yolo train success")