import numpy as np
import cv2

cap = cv2.VideoCapture('../Deep_Learning_OpenCV/images/shore.mov')

if cap.isOpened() == False:
    print('Cannot open file of video stream')


while True:
    ret, frame = cap.read()

    if ret == True:
        cv2.imshow('Frame', frame)

        #default frame settings 25 milisecond
        #esc tuşuna basıldığında kapat
        if cv2.waitKey(25) & 0XFF == 27:
            break

    else:
        break
