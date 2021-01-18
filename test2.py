import cv2

cap = cv2.VideoCapture(0)
cap2 = cv2.VideoCapture(2)
while True:
    ret1, img1 = cap.read()
    ret2, img2 = cap2.read()

    cv2.imshow('cap', img1)
    cv2.imshow('cap2', img2)

    if cv2.waitKey(10) & 0xFF == ord('q'):
        break
