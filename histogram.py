import cv2
import numpy as np

img=cv2.imread("any_photo.jpg",0)
hist=cv2.equalizeHist(img)

img=cv2.imread("any_photo2.jpg")

yuv=cv2.cvtColor(img,cv2.COLOR_BGR2YUV)
yuv=[:,:,0] = cv2.equalizeHist(yuv[:,:,0])

output=cv2.cvtColor(yuv,cv2.COLOR_YUV2BGR)

cv2.imshow("input ",img)
cv2.imshow("equalized",output)

cv2.waitKey()