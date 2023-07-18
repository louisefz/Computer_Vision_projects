import cv2
import numpy as np



cap = cv2.VideoCapture('/Users/zhoujie/Desktop/video/3.mp4')
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
size = (frame_width, frame_height*2)

out = cv2.VideoWriter('/Users/zhoujie/Desktop/video/3_out.mp4',
                         cv2.VideoWriter_fourcc(*'mp4v'),
                         15, size)

font = cv2.FONT_HERSHEY_SIMPLEX
# Define color range for object detection (in RGB color space)
lower_color = (98, 50, 50)
upper_color = (139, 255, 255)
lower_color2 = (100, 50, 50)
upper_color2 = (140, 255, 255)
lower_color3 = (105, 50, 50)
upper_color3 = (120, 255, 255)

# Define kernel for morphological operations
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (15, 15))

f = 0
while True:
    # Read a frame from the video file
    ret, frame = cap.read()

    if not ret:
        # End of video file
        break
    f += 1

    # Convert frame to HSV color space
    if f <= 25:
        hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)


        # Threshold the frame to obtain binary image
        mask = cv2.inRange(hsv_frame, lower_color, upper_color)


        # Perform morphological operations on the binary image
        mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
        mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
        mask = cv2.morphologyEx(mask, cv2.MORPH_DILATE, kernel)
        # print(mask.shape)

        # Display the binary image with the foreground object in white and background in black
        result = cv2.bitwise_and(frame, frame, mask=mask)
        cv2.putText(result, 'RGB_lower: (98, 50, 50)', (10, 30), font, 0.5, (255, 255, 255))
        cv2.putText(result, 'RGB_upper: (139, 255, 255)', (10, 50), font, 0.5, (255, 255, 255))
        cv2.putText(result, 'both sea and sky can be seen', (10, 70), font, 0.5, (255, 255, 255))
        cv2.putText(result, '2.3 Grab object in RGB and HSV', (10,  100), font, 1, (255, 255, 255))
        # print(result.shape)
        result[mask == 0] = (0, 0, 0)
        concat_img = np.concatenate((result, frame), axis=0)
    elif f > 25 and f<=50:
        hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)


        # Threshold the frame to obtain binary image
        mask = cv2.inRange(hsv_frame, lower_color2, upper_color2)


        # Perform morphological operations on the binary image
        mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
        mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
        mask = cv2.morphologyEx(mask, cv2.MORPH_DILATE, kernel)
        # print(mask.shape)

        # Display the binary image with the foreground object in white and background in black
        result = cv2.bitwise_and(frame, frame, mask=mask)
        cv2.putText(result, 'RGB_lower: (98, 50, 50)', (10, 30), font, 0.5, (255, 255, 255))
        cv2.putText(result, 'RGB_upper: (139, 255, 255)', (10, 50), font, 0.5, (255, 255, 255))
        cv2.putText(result, 'part of sea and whole sky can be seen', (10, 70), font, 0.5, (255, 255, 255))
        cv2.putText(result, '2.3 Grab object in RGB and HSV', (10, 100), font, 1, (255, 255, 255))
        print(result.shape)
        result[mask == 0] = (0, 0, 0)
        concat_img = np.concatenate((result, frame), axis=0)
    elif f > 50:
        hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)


        # Threshold the frame to obtain binary image
        mask = cv2.inRange(hsv_frame, lower_color3, upper_color3)


        # Perform morphological operations on the binary image
        mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
        mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
        mask = cv2.morphologyEx(mask, cv2.MORPH_DILATE, kernel)
        # print(mask.shape)

        # Display the binary image with the foreground object in white and background in black
        result = cv2.bitwise_and(frame, frame, mask=mask)
        cv2.putText(result, 'RGB_lower: (98, 50, 50)', (10, 30), font, 0.5, (255, 255, 255))
        cv2.putText(result, 'RGB_upper: (139, 255, 255)', (10, 50), font, 0.5, (255, 255, 255))
        cv2.putText(result, 'only sky can be seen', (10, 70), font, 0.5, (255, 255, 255))
        cv2.putText(result, '2.3 Grab object in RGB and HSV', (10, 100), font, 1, (255, 255, 255))
        # print(result.shape)
        result[mask == 0] = (0, 0, 0)
        concat_img = np.concatenate((result, frame), axis=0)

    out.write(concat_img)

    # Display the original frame and processed result
    cv2.imshow('Original', frame)
    cv2.imshow('Result', result)


    if cv2.waitKey(1) == 27:
        break

# Release the video file and close all windows
# cap.release()
out.release()
cv2.destroyAllWindows()


"""
1. cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) to Convert frame to HSV color space
2. set a RBG range to filter blue things like the sea and the sky
3. tweak the range to filter the only the sea

"""