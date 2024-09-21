import cv2
import numpy as np

img=cv2.imread("any_image.jpg")
rows,cols=img.shape

##sobel filter

horizontal1=cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)
horizontal2=cv2.Sobel(img,cv2.CV_64F,2,0,ksize=5)
horizontal3=cv2.Sobel(img,cv2.CV_64F,3,0,ksize=5)
vertical=cv2.Sobel(img,cv2.CV_64F,0,1,ksize=5)

#laplacian filter

laplacian=cv2.Laplacian(img,cv2.CV_64F)

#canny filter
canny=cv2.Canny(img,50,240)

cv2.imshow("img",img)
cv2.imshow("laplacian",laplacian)
cv2.imshow("canny",canny)

cv2.waitKey()