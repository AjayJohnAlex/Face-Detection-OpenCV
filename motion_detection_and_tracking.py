import cv2
import numpy as np
import matplotlib.pyplot as plt


def callback(x):
    pass


cap = cv2.VideoCapture(0)
cv2.namedWindow("Tracking the HSV value")
cv2.createTrackbar("LH", "Tracking the HSV value", 0, 255, callback)
cv2.createTrackbar("LS", "Tracking the HSV value", 0, 255, callback)
cv2.createTrackbar("LV", "Tracking the HSV value", 0, 255, callback)
cv2.createTrackbar("UH", "Tracking the HSV value", 255, 255, callback)
cv2.createTrackbar("US", "Tracking the HSV value", 255, 255, callback)
cv2.createTrackbar("UV", "Tracking the HSV value", 255, 255, callback)

while True:

    _, frame = cap.read()
    # img = cv2.imread("openCV.jpg")

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    l_h = cv2.getTrackbarPos("LH", "Tracking the HSV value")
    l_s = cv2.getTrackbarPos("LS", "Tracking the HSV value")
    l_v = cv2.getTrackbarPos("LV", "Tracking the HSV value")

    u_h = cv2.getTrackbarPos("UH", "Tracking the HSV value")
    u_s = cv2.getTrackbarPos("US", "Tracking the HSV value")
    u_v = cv2.getTrackbarPos("UV", "Tracking the HSV value")

    l_b = np.array([l_h, l_s, l_v])
    u_b = np.array([u_h, u_s, u_v])

    mask = cv2.inRange(hsv, l_b, u_b)

    res = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow("main_img", frame)
    cv2.imshow("mask", mask)
    cv2.imshow("result", res)

    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()
