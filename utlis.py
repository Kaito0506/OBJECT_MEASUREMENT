import cv2 
import numpy as np


def getCountours(img, threshold=[100, 100], showCanny=True, minArea=1000, filter=0, drawContour=True):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray,(5,5), 1)
    canny = cv2.Canny(blur, threshold[0], threshold[1] )
    ################################################################
    kernel = np.ones((5,5))
    dial = cv2.dilate(canny, kernel, iterations=3)
    imgThreshold = cv2.erode(dial, kernel, iterations=2)
    contours, hiearchy = cv2.findContours(imgThreshold, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    finalContour = []
    ################################################################
    for contour in contours:
        area = cv2.contourArea(contour) #tim xu
        if area > minArea:
            perimeter = cv2.arcLength(contour, True) #tim chu vi cua hinh
            approximation = cv2.approxPolyDP(contour, 0.02*perimeter, True) # lam cho cac edges tro nen thang hang
            bbox = cv2.boundingRect(approximation) # return 4 values x, y , heigth and width
            if filter > 0:
                if len(approximation) == filter:
                    finalContour.append([len(approximation), area, approximation, bbox, contour])
                else:
                    finalContour.append([len(approximation), area, approximation, bbox, contour])
    ###sort out contours 
    finalContour = sorted(finalContour, key= lambda x:x[1], reverse=True) #reverse=True is decending order, we sort base on the area 
    if drawContour:
        for con in finalContour:
            cv2.drawContours(img, con[4], -1, (0,0,255), 4)
            
    if showCanny:
        cv2.imshow("canny", canny)
    return img, finalContour
        
################################

def reorder(points):
    print(points.shape)
    newPoint = np.zeros_like(points)
    points = points.reshape((4,2))
    add = points.sum(1)
    newPoint[0] = points[np.argmin(add)]            
    newPoint[3] = points[np.argmax(add)]   
    diff = np.diff(points, axis=1)
    newPoint[2] = points[np.argmin(diff)]
    newPoint[3] = points[np.argmax(diff)]   
    return newPoint

def wrapImage(img, points, w, h):
    # reorder(points)
    print("hello")
    # print(reorder(points=points)) 
    
