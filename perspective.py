import cv2
import numpy as np

img=cv2.imrread("any_photo.jpg")
rows_cols=img.shape[:2]

source_points=np.float32([[100,100],[1354,1453],[1461,2024],[1071,2024]]) # i choose this point you can chane this
dst_points=np.float32([[0,0],[480,0],[0,640],[480,640]])

matrix=cv2.getPerspectiveTransform(source_points,dst_points)

output=cv2.warpPerspective(img,matrix,(480,640))

cv2.imshow("output",output)
cv2.waitKey()