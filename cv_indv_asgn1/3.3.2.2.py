import cv2
import numpy as np
import random

# Load image
img = cv2.VideoCapture("/Users/zhoujie/Desktop/video/6_2_out.mp4")
# print(img.get(7))
frame_width = int(img.get(3))
frame_height = int(img.get(4))
size = (frame_width, frame_height)
# print(size)
out = cv2.VideoWriter('/Users/zhoujie/Desktop/video/6_1_out.mp4',
                         cv2.VideoWriter_fourcc(*'mp4v'),
                         20, size)
font = cv2.FONT_HERSHEY_SIMPLEX
while True:
    # Read a frame from the video file
    ret, frame = img.read()

    if not ret:
        # End of video file
        break
    cv2.putText(frame, 'The white fan center axis is as reference ', (10, frame_height-90), font, 0.4, (255, 255, 255))
    cv2.putText(frame, 'compare features of each pixel with the the reference axis using MSE', (10, frame_height-70), font, 0.4, (255, 255, 255))
    cv2.putText(frame, 'MSE>0.00000000001 0-black blur.itemset((yp, xp), 0)', (10, frame_height-50), font, 0.4,
                (255, 255, 255))
    cv2.putText(frame, 'MSE<=0.00000000001 255-white blur.itemset((yp, xp), 255)', (10, frame_height-30), font, 0.4,
                (255, 255, 255))
    cv2.putText(frame, 'cv2.HoughCircles() parameter: (1, 140, 15, 75, 6, 58)', (10, frame_height-10), font, 0.4,
                (255, 255, 255))
    cv2.putText(frame, '3.3.2: Feature Detection (MSE)', (10, frame_height - 150), font, 1,
                (255, 255, 255))
    out.write(frame)

