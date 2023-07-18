
# change the blue into red
import cv2
import numpy as np

# Define the color ranges for detection
# color_ranges = [
#     ((200, 80, 40), (255, 120, 190), "red"),  # Red color range
#
#     ((100, 80, 110), (139, 255, 255), "blue")  # Blue color range
# ]

lower_blue = np.array([100, 80, 110])
upper_blue = np.array([139, 255, 255])
red = (0, 0, 255)
# Create a video capture object to read from the webcam
cap = cv2.VideoCapture("/Users/zhoujie/Desktop/video/7_2.mp4")
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
size = (frame_width, frame_height)
print(size)

out = cv2.VideoWriter('/Users/zhoujie/Desktop/video/7_2_out.mp4', cv2.VideoWriter_fourcc(*'mp4v'), 30, size)
font = cv2.FONT_HERSHEY_SIMPLEX



# Start a loop to read frames from the video
while True:
    # Read a frame from the video

    ret, frame = cap.read()
    if ret == False:
        break




    # Convert the frame from BGR to HSV color space
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    res = cv2.bitwise_and(frame, frame, mask=mask)
    res = frame.copy()
    res[mask > 0] = (red)
    cv2.putText(res, '4.2 Freestyle-2', (10, 50), font, 1, (255, 255, 255))
    cv2.putText(res, 'change the blue into red', (10, 20), font, 0.4, (255, 255, 255))

    out.write(res)
    cv2.imshow("frame", frame)
    cv2.imshow('frame', res)

    if cv2.waitKey(25) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()







