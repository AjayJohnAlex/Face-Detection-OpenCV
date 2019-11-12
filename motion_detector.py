import cv2
import numpy as np
# from google.colab.patches import cv2_imshow

cap = cv2.VideoCapture(0)

_, frame1 = cap.read()
_, frame2 = cap.read()

while cap.isOpened():

    difference = cv2.absdiff(frame1, frame2)
    gray = cv2.cvtColor(difference, cv2.COLOR_BGR2GRAY)
    blur_img = cv2.GaussianBlur(gray, (5, 5), 0)
    print("mean", np.mean(frame1))
    _, threshold = cv2.threshold(blur_img, 25, 255, cv2.THRESH_BINARY)
    dilate = cv2.dilate(threshold, None, iterations=3)
    contours, _ = cv2.findContours(dilate, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# TO draw contours around the image
    cv2.drawContours(frame1,contours,-1,(255,0,0),2)
# =============================================================================
#    TO draw rectange around the contours obtained
#    
#     for contour in contours:
# 
#         (x, y, w, h) = cv2.boundingRect(contour)
# 
#         if cv2.contourArea(contour) < 900:
#             continue
#     
#         rectangele_img = cv2.rectangle(frame1, (x, y), (x + w, y + h), (0, 255, 0), 3)
#         cv2.putText(frame1, "status : {}".format("movement"),(10, 10), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 2)
# 
# =============================================================================
    cv2.imshow("frame",frame1)
    frame1 = frame2
    _, frame2 = cap.read()

    if cv2.waitKey(40) == 27:
        break

cv2.destroyAllWindows()
cap.release()
