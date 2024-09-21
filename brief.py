import cv2
import numpy as np

cap = cv2.VideoCapture(0)
fast = cv2.FastFeatureDetector_create()  # Güncellenmiş FAST detektör kullanımı
brief = cv2.xfeatures2d.BriefDescriptorExtractor_create()  # BRIEF çıkarıcı

while True:
    ret, frame = cap.read()
    keypoints = fast.detect(frame, None)
    
    keypoints, descriptors = brief.compute(frame, keypoints)

    keypoints1 = cv2.drawKeypoints(frame, keypoints, color=(255, 255, 255))
    cv2.imshow("BRIEF", keypoints1)

    q = cv2.waitKey(1)  # Her döngüde pencerede güncelleme yapması için 1 vermek

    if q == 27:  # ESC tuşu ile çıkış
        break

cap.release()
cv2.destroyAllWindows()
