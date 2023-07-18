# replace the blue colour part with another object

import cv2
import numpy as np

# Load video
cap = cv2.VideoCapture("/Users/zhoujie/Desktop/video/7_3.mp4")
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
size = (frame_width, frame_height)
print(size)

out = cv2.VideoWriter('/Users/zhoujie/Desktop/video/7_3_out.mp4', cv2.VideoWriter_fourcc(*'mp4v'), 25, size)
font = cv2.FONT_HERSHEY_SIMPLEX

# Define range of blue color in HSV
lower_blue = np.array([100, 50, 50])
upper_blue = np.array([130, 255, 255])

# Define red color in RGB
red = (0, 0, 255)

# Define triangle vertices
pts = np.array([[0, 0], [20, 20], [0, 20]], np.int32)

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == False:
        break
    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Threshold the HSV image to get only blue colors
    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    # Find contours of blue objects
    contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Draw a red triangle on the blue object
    for cnt in contours:
        # Get the moments of the contour
        M = cv2.moments(cnt)
        if M['m00'] != 0:

            # Get the centroid of the contour
            cx = int(M['m10']/M['m00'])
            cy = int(M['m01']/M['m00'])

        # Draw a red triangle on the centroid
            cv2.fillPoly(frame, [pts + [cx, cy]], red)

        # Display the resulting frame
    cv2.putText(frame, '4.3 Freestyle-3', (10, 50), font, 1, (255, 255, 255))
    cv2.putText(frame, 'cover the blue objects with red triangles', (10, 20), font, 0.4, (255, 255, 255))
    out.write(frame)
    cv2.imshow('frame',frame)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break


# Release video and close windows
cap.release()
cv2.destroyAllWindows()
