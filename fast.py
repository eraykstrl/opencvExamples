import cv2
import numpy as np

cap=cv2.VideoCapture(0)
fast=cv2.FastFeatureDetector_create()
while True:
    ret,frame=cap.read()
    keypoints=fast.detect(frame,None)
    nonmax=cv2.drawKeypoints(frame,keypoints,color=(255,255,255))
    cv2.imshow("fast",nonmax)
    

    q=cv2.waitKey()
    if q == 27:
        break

cap.release()
cv2.destroyAllWindows()

