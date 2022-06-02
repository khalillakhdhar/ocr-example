import os
import easyocr
import cv2
import time
from matplotlib import pyplot as plt
import numpy as np


cap = cv2.VideoCapture(0)
count = 0
reader = easyocr.Reader(['ar'])
IMAGE_PATH = './frame1.jpg'

while cap.isOpened():
    ret,frame = cap.read()
    if ret == True:
        cv2.imshow('window-name',frame)
        cv2.imwrite("./frame1.jpg", frame)
        
        
        result = reader.readtext(IMAGE_PATH,paragraph="False")
        text = result[0][1]
        print(text)
        #count = count + 1
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break
    else:
        break
cap.release()
cv2.destroyAllWindows()

