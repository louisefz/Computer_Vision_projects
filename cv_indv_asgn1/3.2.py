import cv2
import numpy as np
import random

# Load image
img = cv2.VideoCapture('/Users/zhoujie/Desktop/video/5.mp4')
frame_width = int(img.get(3))
frame_height = int(img.get(4))
size = (frame_width, frame_height)
print(size)
out = cv2.VideoWriter('/Users/zhoujie/Desktop/video/5_out.mp4',
                         cv2.VideoWriter_fourcc(*'mp4v'),
                         20, size)

# Convert image to grayscale


font = cv2.FONT_HERSHEY_SIMPLEX

q = 0
# Automatically tweak Hough transform parameters by using for loop
while True:
    # Read a frame from the video file
    ret, frame = img.read()
    q += 1

    if not ret:
        # End of video file
        break
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    if q <= 40:
    # Blur image to reduce noise
        blur = cv2.GaussianBlur(gray, (5, 5), 0)
        # Detect circles using Hough transform
        dp = 1#random.randrange(1, 3)
        minDist = 120#random.randrange(120, 150, 10)
        param1 = 10#random.randrange(10, 20, 5)
        param2 = 40#random.randrange(40, 50, 5)
        minRadius = 2#random.randrange(2, 10, 2)
        maxRadius = 40#random.randrange(40, 55, 2)
        print((dp, minDist, param1, param2, minRadius, maxRadius))


        circles = cv2.HoughCircles(blur, cv2.HOUGH_GRADIENT, dp=dp, minDist=minDist,
                                   param1=param1, param2=param2, minRadius=minRadius,
                                   maxRadius=maxRadius)
        if circles is not None:
            circles = np.round(circles[0, :]).astype("int")
            for (x, y, r) in circles:
                cv2.circle(frame, (x, y), r, (0, 255, 0), 2)
            cv2.putText(frame, "dp: 1", (10, 10), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (255, 255, 255), 1)
            cv2.putText(frame, "minDist: 120", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (255, 255, 255), 1)
            cv2.putText(frame, "param1: 10", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (255, 255, 255), 1)
            cv2.putText(frame, "param2: 40", (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (255, 255, 255), 1)
            cv2.putText(frame, "minRadius: 2", (10, 90), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (255, 255, 255), 1)
            cv2.putText(frame, "maxRadius: 40", (10, 110), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (255, 255, 255), 1)
            cv2.putText(frame, "the best case", (10, 140), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 1)
            cv2.putText(frame, "3.2 Hough transform", (10, 180), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 1)
            out.write(frame)
    elif q > 40 and q<= 80:
    # Blur image to reduce noise
        blur = cv2.GaussianBlur(gray, (5, 5), 0)
        # Detect circles using Hough transform
        dp = 2#random.randrange(1, 3)
        minDist = 120#random.randrange(120, 150, 10)
        param1 = 15#random.randrange(10, 20, 5)
        param2 = 45#random.randrange(40, 50, 5)
        minRadius = 4#random.randrange(2, 10, 2)
        maxRadius = 47#random.randrange(40, 55, 2)
        print((dp, minDist, param1, param2, minRadius, maxRadius))


        circles = cv2.HoughCircles(blur, cv2.HOUGH_GRADIENT, dp=dp, minDist=minDist,
                                   param1=param1, param2=param2, minRadius=minRadius,
                                   maxRadius=maxRadius)
        if circles is not None:
            circles = np.round(circles[0, :]).astype("int")
            for (x, y, r) in circles:
                cv2.circle(frame, (x, y), r, (0, 255, 0), 2)
            cv2.putText(frame, "dp: 2", (10, 10), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (255, 255, 255), 1)
            cv2.putText(frame, "minDist: 120", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (255, 255, 255), 1)
            cv2.putText(frame, "param1: 15", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (255, 255, 255), 1)
            cv2.putText(frame, "param2: 45", (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (255, 255, 255), 1)
            cv2.putText(frame, "minRadius: 4", (10, 90), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (255, 255, 255), 1)
            cv2.putText(frame, "maxRadius: 47", (10, 110), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (255, 255, 255), 1)
            cv2.putText(frame, "3.2 Hough transform", (10, 180), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 1)
            out.write(frame)
    elif q > 80 and q<= 120:
    # Blur image to reduce noise
        blur = cv2.GaussianBlur(gray, (5, 5), 0)
        # Detect circles using Hough transform
        dp = 3#random.randrange(1, 3)
        minDist = 140#random.randrange(120, 150, 10)
        param1 = 18#random.randrange(10, 20, 5)
        param2 = 30#random.randrange(40, 50, 5)
        minRadius = 5#random.randrange(2, 10, 2)
        maxRadius = 49#random.randrange(40, 55, 2)
        print((dp, minDist, param1, param2, minRadius, maxRadius))

        circles = cv2.HoughCircles(blur, cv2.HOUGH_GRADIENT, dp=dp, minDist=minDist,
                                   param1=param1, param2=param2, minRadius=minRadius,
                                   maxRadius=maxRadius)
        if circles is not None:
            circles = np.round(circles[0, :]).astype("int")
            for (x, y, r) in circles:
                cv2.circle(frame, (x, y), r, (0, 255, 0), 2)
            cv2.putText(frame, "dp: 3", (10, 10), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (255, 255, 255), 1)
            cv2.putText(frame, "minDist: 140", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (255, 255, 255), 1)
            cv2.putText(frame, "param1: 18", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (255, 255, 255), 1)
            cv2.putText(frame, "param2: 30", (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (255, 255, 255), 1)
            cv2.putText(frame, "minRadius: 5", (10, 90), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (255, 255, 255), 1)
            cv2.putText(frame, "maxRadius: 49", (10, 110), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (255, 255, 255), 1)
            cv2.putText(frame, "3.2 Hough transform", (10, 180), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 1)
            out.write(frame)
    elif q > 120 and q<= 160:
    # Blur image to reduce noise
        blur = cv2.GaussianBlur(gray, (5, 5), 0)
        # Detect circles using Hough transform
        dp = 1#random.randrange(1, 3)
        minDist = 140#random.randrange(120, 150, 10)
        param1 = 10#random.randrange(10, 20, 5)
        param2 = 40#random.randrange(40, 50, 5)
        minRadius = 8#random.randrange(2, 10, 2)
        maxRadius = 55#random.randrange(40, 55, 2)
        # print((dp, minDist, param1, param2, minRadius, maxRadius))


        circles = cv2.HoughCircles(blur, cv2.HOUGH_GRADIENT, dp=dp, minDist=minDist,
                                           param1=param1, param2=param2, minRadius=minRadius,
                                           maxRadius=maxRadius)
        if circles is not None:
            circles = np.round(circles[0, :]).astype("int")
            for (x, y, r) in circles:
                cv2.circle(frame, (x, y), r, (0, 255, 0), 2)
            cv2.putText(frame, "dp: 1", (10, 10), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (255, 255, 255), 1)
            cv2.putText(frame, "minDist: 140", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (255, 255, 255), 1)
            cv2.putText(frame, "param1: 10", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (255, 255, 255), 1)
            cv2.putText(frame, "param2: 40", (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (255, 255, 255), 1)
            cv2.putText(frame, "minRadius: 8", (10, 90), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (255, 255, 255), 1)
            cv2.putText(frame, "maxRadius: 55", (10, 110), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (255, 255, 255), 1)
            cv2.putText(frame, "3.2 Hough transform", (10, 180), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 1)

            out.write(frame)
    # print(circles)
    elif q > 160:
    # Blur image to reduce noise
        blur = cv2.GaussianBlur(gray, (5, 5), 0)
        # Detect circles using Hough transform
        dp = 1#random.randrange(1, 3)
        minDist = 120#random.randrange(120, 150, 10)
        param1 = 20#random.randrange(10, 20, 5)
        param2 = 50#random.randrange(40, 50, 5)
        minRadius = 30#random.randrange(2, 10, 2)
        maxRadius = 40#random.randrange(40, 55, 2)
        print((dp, minDist, param1, param2, minRadius, maxRadius))


        circles = cv2.HoughCircles(blur, cv2.HOUGH_GRADIENT, dp=dp, minDist=minDist,
                                   param1=param1, param2=param2, minRadius=minRadius,
                                   maxRadius=maxRadius)
        if circles is not None:
            circles = np.round(circles[0, :]).astype("int")
            for (x, y, r) in circles:
                cv2.circle(frame, (x, y), r, (0, 255, 0), 2)
            cv2.putText(frame, "dp: 1", (10, 10), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (255, 255, 255), 1)
            cv2.putText(frame, "minDist: 140", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (255, 255, 255), 1)
            cv2.putText(frame, "param1: 10", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (255, 255, 255), 1)
            cv2.putText(frame, "param2: 40", (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (255, 255, 255), 1)
            cv2.putText(frame, "minRadius: 8", (10, 90), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (255, 255, 255), 1)
            cv2.putText(frame, "maxRadius: 55", (10, 110), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (255, 255, 255), 1)
            cv2.putText(frame, "3.2 Hough transform", (10, 180), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 1)
            out.write(frame)

    # Draw circles on the original image

        # Display the resulting image with flashy contours
        cv2.imshow('Circles detected', frame)
        if cv2.waitKey(1) == 27:
            break

# Close all windows
cv2.destroyAllWindows()

"""
1.  cv2.HoughCircles() is used and some parameters are tweaked
(1, 120, 10, 40, 2, 40)  效果最佳
(2, 120, 15, 45, 4, 47)
(2, 120, 15, 45, 4, 47)
(3, 140, 18, 30, 5, 49)
(1, 120, 20, 50, 30, 40) 


"""



