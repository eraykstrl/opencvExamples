import cv2

right = cv2.CascadeClassifier("right_ear_cascade.xml")
left = cv2.CascadeClassifier("left_ear_cascade.xml")  # These cascades are examples

if right.empty():
    print("There is no right ear cascade")

if left.empty():
    print("There is no left ear cascade")

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    frame = cv2.resize(frame, (640, 480), interpolation=cv2.INTER_AREA)

    right_ear = right.detectMultiScale(frame, 1.5, 5)
    left_ear = left.detectMultiScale(frame, 1.5, 5)

    for (x, y, w, h) in right_ear:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 255, 255), 2)

    for (x, y, w, h) in left_ear:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 255, 255), 2)

    cv2.imshow('Ear Detection', frame)  # Add a title for the window

    q = cv2.waitKey(1)  # Change to 1 for continuous loop

    if q == 27:  # ESC key to exit
        break

cap.release()
cv2.destroyAllWindows()
