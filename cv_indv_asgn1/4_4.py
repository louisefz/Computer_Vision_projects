# detect the circles and change the cicle colour with red

import cv2
import numpy as np

# Load video
cap = cv2.VideoCapture("/Users/zhoujie/Desktop/video/7_4.mp4")
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
size = (frame_width, frame_height)
print(size)

out = cv2.VideoWriter('/Users/zhoujie/Desktop/video/7_4_out.mp4', cv2.VideoWriter_fourcc(*'mp4v'), 30, size)
font = cv2.FONT_HERSHEY_SIMPLEX

# Define parameters for circle detection
min_radius = 10
max_radius = 50
dp = 1
min_dist = 50
canny_thresh = 50
acc_thresh = 30

# Define red color in RGB
red = (0, 0, 255)

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        # Convert frame to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Apply Gaussian blur to reduce noise
        gray = cv2.GaussianBlur(gray, (5, 5), 0)

        # Apply Hough circle detection to find circles
        circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, dp, min_dist, param1=canny_thresh, param2=acc_thresh, minRadius=min_radius, maxRadius=max_radius)

        # Fill detected circles with red color
        if circles is not None:
            circles = np.round(circles[0, :]).astype("int")
            for (x, y, r) in circles:
                cv2.circle(frame, (x, y), r, red, -1)

        # Display the resulting frame
        cv2.putText(frame, '4.4 Freestyle-4', (10, 50), font, 1, (255, 255, 255))
        cv2.putText(frame, 'detect the circles and color them red', (10, 20), font, 0.4, (255, 255, 255))
        out.write(frame)
        cv2.imshow('frame',frame)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    else:
        break

# Release video and close windows
cap.release()
cv2.destroyAllWindows()
