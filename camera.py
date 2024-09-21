import cv2

cap=cv2.VideoCapture(0)

while True:
    ret,frame=cap.read()
    frame=cv2.resize(frame,(640,480),interpolation=cv2.INTER_AREA)
    cv2.imshow("input",frame)

    q=cv2.waitKey(0)

    if q== 27:
        break


cap.release()
cv2.destroyAllWindows()