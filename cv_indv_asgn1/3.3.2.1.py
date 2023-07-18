import cv2
import numpy as np
import random

# Load image
img = cv2.VideoCapture("/Users/zhoujie/Desktop/video/757.mp4")
# print(img.get(7))
frame_width = int(img.get(3))
frame_height = int(img.get(4))
size = (frame_width, frame_height)
# print(size)
out = cv2.VideoWriter('/Users/zhoujie/Desktop/video/6_2_out.mp4',
                         cv2.VideoWriter_fourcc(*'mp4v'),
                         20, size)

# Convert image to grayscale



dp = 1#random.randrange(1, 2)
minDist = 140#random.randrange(120, 150, 10)
param1 = 15#random.randrange(10, 20, 5)
param2 = 75#random.randrange(70, 80, 5)
minRadius = 6#random.randrange(2, 10, 2)
maxRadius = 58#random.randrange(50, 60, 2)
# print((dp, minDist, param1, param2, minRadius, maxRadius))
q = 0
array_list = []
# Automatically tweak Hough transform parameters by using for loop
while True:
    print("-------")
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

    # print(circles)

    # Draw circles on the original image
    if circles is not None:
        q += 1
        print(q)
        circles = np.round(circles[0, :]).astype("int")
        first_circle = circles[0]
        x = first_circle[0]
        y = first_circle[1]
        r = first_circle[2]

        blur1 = cv2.circle(blur, (x, y), r, (0, 255, 0), 2)

        # cv2.imshow('Thresholded Image', blur1)

        ref_pixel = blur[y,x]
        # print(ref_pixel)
        for yp in range(0,frame.shape[0]):
            for xp in range(0,frame.shape[1]):
                other_pixel = blur[yp,xp]
                # print(other_pixel)x
                mse = np.mean((np.array(ref_pixel) - np.array(other_pixel))**2)
                # print(mse)

                # print(mse)
                if mse > 0.00000000001:
                    blur.itemset((yp, xp), 0)



                else:
                    blur.itemset((yp, xp), 255)
                array_list.append(blur)



                # blur = cv2.merge((blur,blur,blur))
                # print(blur.shape)

    #             new_img = np.concatenate((blur1, blur), axis=1)
        print(blur.shape)
        blurn = cv2.merge((blur,blur,blur))
        out.write(blurn)
        cv2.imshow('Thresholded Image', blurn)



    if cv2.waitKey(1) == 27:
        break


        # print(blur.shape)



# Close all windows
cv2.destroyAllWindows()

"""

1. The white fan's center axis is as reference 
2. compare features of each pixel with the the reference axis using MSE
3. MSE>0.00000000001 0-black blur.itemset((yp, xp), 0)
4. MSE<=0.00000000001 1-white blur.itemset((yp, xp), 255)
5. parameter: (1, 140, 15, 75, 6, 58)

"""

