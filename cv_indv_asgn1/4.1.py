# detect the blue object and draw a rectangular

import cv2
import numpy as np

# Define the color ranges for detection
color_ranges = [
         # Red color range

    ((100, 80, 110), (139, 255, 255), "blue")     # Blue color range
]

# Create a video capture object to read from the webcam
cap = cv2.VideoCapture("/Users/zhoujie/Desktop/video/7_1.mp4")
frame_width = int(cap .get(3))
frame_height = int(cap .get(4))
size = (frame_width, frame_height)
print(size)

out = cv2.VideoWriter('/Users/zhoujie/Desktop/video/7_1_out.mp4', cv2.VideoWriter_fourcc(*'mp4v'), 30, size)

font = cv2.FONT_HERSHEY_SIMPLEX
# Start a loop to read frames from the video
while True:
    # Read a frame from the video
    ret, frame = cap.read()
    if not ret:
        # End of video file
        break

    # Convert the frame from BGR to HSV color space
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Iterate through the color ranges for detection
    for (lower, upper, color_name) in color_ranges:
        # Create a mask for the color range
        mask = cv2.inRange(hsv, lower, upper)


        # Find contours in the mask
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)


        # Iterate through the contours and draw rectangles around them
        for cnt in contours:
            x, y, w, h = cv2.boundingRect(cnt)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(frame, color_name, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

    # Display the annotated frame
    cv2.putText(frame, '4.1 Freestyle-1', (10, 50), font, 1, (255, 255, 255))
    cv2.putText(frame, 'detect the object of blue-coloured', (10, 20), font, 0.4, (255, 255, 255))
    cv2.imshow("frame", frame)
    out.write(frame)

    # Check for key press to exit the loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object and destroy all windows
cap.release()
cv2.destroyAllWindows()
