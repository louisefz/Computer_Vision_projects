import cv2
import numpy as np
import random

# Load image
img = cv2.VideoCapture("/Users/zhoujie/Desktop/video/6.mp4")
frame_width = int(img.get(3))
frame_height = int(img.get(4))
size = (frame_width, frame_height)
# print((size))
out = cv2.VideoWriter('/Users/zhoujie/Desktop/video/6_out.mp4',
                         cv2.VideoWriter_fourcc(*'mp4v'),
                         20, size)
font = cv2.FONT_HERSHEY_SIMPLEX
# Convert image to grayscale

# (1, 140, 15, 75, 6, 58)

dp = 1#random.randrange(1, 2)
minDist = 140#random.randrange(120, 150, 10)
param1 = 15#random.randrange(10, 20, 5)
param2 = 75#random.randrange(70, 80, 5)
minRadius = 6#random.randrange(2, 10, 2)
maxRadius = 58#random.randrange(50, 60, 2)
print((dp, minDist, param1, param2, minRadius, maxRadius))
# Automatically tweak Hough transform parameters by using for loop
while True:
    # Read a frame from the video file
    ret, frame = img.read()

    if not ret:
        # End of video file
        break
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Blur image to reduce noise
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    # Detect circles using Hough transform
    circles = cv2.HoughCircles(blur, cv2.HOUGH_GRADIENT, dp=dp, minDist=minDist,
                               param1=param1, param2=param2, minRadius=minRadius,
                               maxRadius=maxRadius)

    # Draw circles on the original image
    if circles is not None:
        circles = np.round(circles[0, :]).astype("int")
        for (x, y, r) in circles:
            upleft = (x-r-5,y-r-10)
            lowright = (x+r+5,y+r+10)
            cv2.circle(blur, (x, y), r, (0, 255, 0), 2)
            cv2.rectangle(blur, upleft, lowright, (0, 0, 255), 2)
            blurn = cv2.merge((blur,blur,blur))
        cv2.putText(blurn, 'The white fan is detected', (10, 30), font, 0.4, (255, 255, 255))
        cv2.putText(blurn, 'circle detection: cv2.HoughCircles()', (10, 50), font, 0.4, (255, 255, 255))
        cv2.putText(blurn, 'cv2.HoughCircles() parameter: (1, 140, 15, 75, 6, 58)', (10, 70), font, 0.4, (255, 255, 255))
        cv2.putText(blurn, 'cv2.rectangle() is used to draw rectangle with circle center as reference axis', (10, 90), font, 0.4, (255, 255, 255))
        cv2.putText(blurn, "3.3.1 Draw an Retangular", (10, 120), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 1)
        out.write(blurn)
        # Display the resulting image with flashy contours
        cv2.imshow('Circles detected', blurn)
        if cv2.waitKey(1) == 27:
            break



# Close all windows
cv2.destroyAllWindows()


"""
1. The white fan is detected
2. circle detection: cv2.HoughCircles()
3. parameter: (1, 140, 15, 75, 6, 58)
"""
