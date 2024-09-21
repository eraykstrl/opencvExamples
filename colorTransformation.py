import cv2
import numpy as np

img=cv2.imread("any.jpg")

cv2.imshow("image",img)

gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("gray_image",gray_img)

yuv_img=cv2.cvtColor(img,cv2.COLOR_BGR2YUV)
cv2.imshow("yuv_image",yuv_img)

hsv_img=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
cv2.imshow("hsv_image",hsv_img)


cv2.waitKey()

