import cv2
import numpy as np
import utlis  


webcam = True
img_path = r"E:\HOC_TAP\NLCN\CODE\input\test.jpg"

cap = cv2.VideoCapture(1)
cap.set(10, 160) #set brightness
cap.set(3, 500) # height capture
cap.set(4, 500) # width capture

while True:
    #####get input capture########################
    if webcam: 
        ret, frame = cap.read()
    else:
        frame = cv2.imread(img_path)
    ################################################################

    frame = cv2.resize(frame, (500, 500))
    img, contours = utlis.getCountours(frame, showCanny=True, drawContour=True, filter=4, minArea=10000)
    
    if len(contours) != 0:
        biggest_shape = contours[0][2] # get 4 points of approximation
        # print(biggest_shape)
        utlis.wrapImage(img, biggest_shape, 100, 100)
    
    cv2.imshow("original", frame)
    
    cv2.waitKey(1)
    
    