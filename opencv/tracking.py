import cv2
import numpy as np
# image=cv2.imread('circles.jpg',1)
# cv2.imshow('original',image)
cap=cv2.VideoCapture(0)
while(1):
    _,frame=cap.read()
    new_image=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    cv2.imshow('image',new_image)

    lower_bound=np.array([110,50,50])
    upper_bound=np.array([130,252,252])
    mask=cv2.inRange(new_image,lower_bound,upper_bound)
    cv2.imshow('mask',mask)

    res=cv2.bitwise_and(frame,frame,mask=mask)
    cv2.imshow('result',res)

# blue=np.uint8([[[255,0,0]]])
# hsv_blue=cv2.cvtColor(blue,cv2.COLOR_BGR2HSV)
# print(hsv_blue)
    if cv2.waitKey(20) & 0xFF == 27:
        break


cv2.destroyAllWindows()