import cv2
import numpy as np

img=cv2.imread("any_img.jpg")
img=cv2.resize(img,(640,480),interpolation=cv2.INTER_AREA)

img_gauss=cv2.GaussianBlur(img,(15,15),0)
bilateral=cv2.bilateralFilter(img,15,50,50)

cv2.imshow("original",img)
cv2.imshow("gauss",img_gauss)
cv2.imshow("bilateral",bilateral)

cv2.waitKey()