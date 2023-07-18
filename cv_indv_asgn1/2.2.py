import cv2
import numpy as np

frame1 = cv2.VideoCapture("/Users/zhoujie/Desktop/video/2.mp4")
frame_width = int(frame1 .get(3))
height = int(frame1 .get(4))
size = (frame_width, height*2)
print(size)


out1 = cv2.VideoWriter('/Users/zhoujie/Desktop/video/2_out.mp4', cv2.VideoWriter_fourcc(*'mp4v'), 20, size)


font = cv2.FONT_HERSHEY_SIMPLEX
f = 0
while True:
    # Read a frame from the video file
    ret, frame = frame1.read()
    f += 1

    if not ret:
        # End of video file
        break
    if f <= 20:
        ksize = 1

 #一帧的所有knenal遍历完之后，进行下一帧 10, 20, 50, 80
        # Apply Gaussian filter
        gframe1 = cv2.GaussianBlur(frame, (ksize, ksize), 0)
        cv2.putText(gframe1, 'Gaussian filters', (10, 30), font, 0.5, (255, 255, 255))
        cv2.putText(gframe1, 'ksize = 1', (10, 50), font, 0.5, (255, 255, 255))


        # Apply bilateral filter
        bframe1 = cv2.bilateralFilter(frame, ksize, 75, 75)
        cv2.putText(bframe1, 'Bilateral filters', (10, height-30), font, 0.5, (255, 255, 255))
        cv2.putText(bframe1, 'ksize = 1', (10, height-50), font, 0.5, (255, 255, 255))
        cv2.putText(bframe1, '2.2 Smoothing or Blurring', (10, height - 200), font, 1, (255, 255, 255))


        # add_two frames
        added_image1 = np.concatenate((gframe1, bframe1), axis=0)

        out1.write(added_image1)
    elif f>20 and f<=40:
        ksize = 11
        gframe1 = cv2.GaussianBlur(frame, (ksize, ksize), 0)
        cv2.putText(gframe1, 'Gaussian filters', (10, 30), font, 0.5, (255, 255, 255))
        cv2.putText(gframe1, 'ksize = 11', (10, 50), font, 0.5, (255, 255, 255))
        cv2.putText(gframe1, 'Gaussian-processed img getting more fuzzy', (10, 70), font, 0.5, (255, 255, 255))
        cv2.putText(gframe1, 'because the Gaussian filter only considers spatial proximity', (10, 90), font, 0.5, (255, 255, 255))
        # Apply bilateral filter
        bframe1 = cv2.bilateralFilter(frame, ksize, 75, 75)
        cv2.putText(bframe1, 'Bilateral filters', (10, height-30), font, 0.5, (255, 255, 255))
        cv2.putText(bframe1, 'ksize = 11', (10, height-50), font, 0.5, (255, 255, 255))
        cv2.putText(bframe1, '2.2 Smoothing or Blurring', (10, height - 200), font, 1, (255, 255, 255))
        # add_two frames
        added_image1 = np.concatenate((gframe1, bframe1), axis=0)
        out1.write(added_image1)
    elif f>40 and f<=60:
        ksize = 31
        gframe1 = cv2.GaussianBlur(frame, (ksize, ksize), 0)
        cv2.putText(gframe1, 'Gaussian filters', (10, 30), font, 0.5, (255, 255, 255))
        cv2.putText(gframe1, 'ksize = 31', (10, 50), font, 0.5, (255, 255, 255))
        cv2.putText(gframe1, 'Gaussian-processed img getting more fuzzy', (10, 70), font, 0.5, (255, 255, 255))
        cv2.putText(gframe1, 'because the Gaussian filter only considers spatial proximity', (10, 90), font, 0.5, (255, 255, 255))
        # Apply bilateral filter
        bframe1 = cv2.bilateralFilter(frame, ksize, 75, 75)
        cv2.putText(bframe1, 'Bilateral filters', (10, height-30), font, 0.5, (255, 255, 255))
        cv2.putText(bframe1, 'ksize = 31', (10, height-50), font, 0.5, (255, 255, 255))
        cv2.putText(bframe1, '2.2 Smoothing or Blurring', (10, height - 200), font, 1, (255, 255, 255))
        # add_two frames
        added_image1 = np.concatenate((gframe1, bframe1), axis=0)
    elif f>60 and f<=80:
        ksize = 41
        gframe1 = cv2.GaussianBlur(frame, (ksize, ksize), 0)
        cv2.putText(gframe1, 'Gaussian filters', (10, 30), font, 0.5, (255, 255, 255))
        cv2.putText(gframe1, 'ksize = 41', (10, 50), font, 0.5, (255, 255, 255))
        cv2.putText(gframe1, 'Gaussian-processed img getting more fuzzy', (10, 70), font, 0.5, (255, 255, 255))
        cv2.putText(gframe1, 'because the Gaussian filter only considers spatial proximity', (10, 90), font, 0.5, (255, 255, 255))
        # Apply bilateral filter
        bframe1 = cv2.bilateralFilter(frame, ksize, 75, 75)
        cv2.putText(bframe1, 'Bilateral filters', (10, height-30), font, 0.5, (255, 255, 255))
        cv2.putText(bframe1, 'ksize = 41', (10, height-50), font, 0.5, (255, 255, 255))
        cv2.putText(bframe1, '2.2 Smoothing or Blurring', (10, height - 200), font, 1, (255, 255, 255))
        # add_two frames
        added_image1 = np.concatenate((gframe1, bframe1), axis=0)
        out1.write(added_image1)
    elif f > 80 and f <= 100:
        ksize = 51
        gframe1 = cv2.GaussianBlur(frame, (ksize, ksize), 0)
        cv2.putText(gframe1, 'Gaussian filters', (10, 30), font, 0.5, (255, 255, 255))
        cv2.putText(gframe1, 'ksize = 51', (10, 50), font, 0.5, (255, 255, 255))
        cv2.putText(gframe1, 'Gaussian-processed img getting more fuzzy', (10, 70), font, 0.5, (255, 255, 255))
        cv2.putText(gframe1, 'because the Gaussian filter only considers spatial proximity', (10, 90), font, 0.5, (255, 255, 255))
        # Apply bilateral filter
        bframe1 = cv2.bilateralFilter(frame, ksize, 75, 75)
        cv2.putText(bframe1, 'Bilateral filters', (10, height-30), font, 0.5, (255, 255, 255))
        cv2.putText(bframe1, 'ksize = 51', (10, height-50), font, 0.5, (255, 255, 255))
        cv2.putText(bframe1, 'Bilateral-processed img is still very clear', (10, height - 70), font, 0.5, (255, 255, 255))
        cv2.putText(bframe1,
                    'Because bilateral filter process spatial proximity and pixel intensity similarity',
                    (10, height - 90), font, 0.4, (255, 255, 255))
        cv2.putText(bframe1, '2.2 Smoothing or Blurring', (10, height - 200), font, 1, (255, 255, 255))
        # add_two frames
        added_image1 = np.concatenate((gframe1, bframe1), axis=0)
        out1.write(added_image1)
    elif f > 100 and f <= 120:
        ksize = 61
        gframe1 = cv2.GaussianBlur(frame, (ksize, ksize), 0)
        cv2.putText(gframe1, 'Gaussian filters', (10, 30), font, 0.5, (255, 255, 255))
        cv2.putText(gframe1, 'ksize = 61', (10, 50), font, 0.5, (255, 255, 255))
        cv2.putText(gframe1, 'Gaussian-processed img getting more fuzzy', (10, 70), font, 0.5, (255, 255, 255))
        cv2.putText(gframe1, 'because the Gaussian filter only considers spatial proximity', (10, 90), font, 0.5, (255, 255, 255))
        # Apply bilateral filter
        bframe1 = cv2.bilateralFilter(frame, ksize, 75, 75)
        cv2.putText(bframe1, 'Bilateral filters', (10, height-30), font, 0.5, (255, 255, 255))
        cv2.putText(bframe1, 'ksize = 61', (10, height-50), font, 0.5, (255, 255, 255))
        cv2.putText(bframe1, 'Bilateral-processed img is still very clear', (10, height - 70), font, 0.5,
                    (255, 255, 255))
        cv2.putText(bframe1,
                    'Because bilateral filter process both spatial proximity and pixel intensity similarity',
                    (10, height - 90), font, 0.4, (255, 255, 255))
        cv2.putText(bframe1, '2.2 Smoothing or Blurring', (10, height - 200), font, 1, (255, 255, 255))
        # add_two frames
        added_image1 = np.concatenate((gframe1, bframe1), axis=0)
    elif f > 120 and f <= 140:
        ksize = 71
        gframe1 = cv2.GaussianBlur(frame, (ksize, ksize), 0)
        cv2.putText(gframe1, 'Gaussian filters', (10, 30), font, 0.5, (255, 255, 255))
        cv2.putText(gframe1, 'ksize = 71', (10, 50), font, 0.5, (255, 255, 255))
        cv2.putText(gframe1, 'Gaussian-processed img getting more fuzzy', (10, 70), font, 0.5, (255, 255, 255))
        cv2.putText(gframe1, 'because the Gaussian filter only considers spatial proximity', (10, 90), font, 0.5,
                    (255, 255, 255))
        # Apply bilateral filter
        bframe1 = cv2.bilateralFilter(frame, ksize, 75, 75)
        cv2.putText(bframe1, 'Bilateral filters', (10, height-30), font, 0.5, (255, 255, 255))
        cv2.putText(bframe1, 'ksize = 71', (10, height-50), font, 0.5, (255, 255, 255))
        cv2.putText(bframe1, 'Bilateral-processed img is still very clear', (10, height - 70), font, 0.5,
                    (255, 255, 255))
        cv2.putText(bframe1,
                    'Because bilateral filter process spatial proximity and pixel intensity similarity',
                    (10, height - 90), font, 0.4, (255, 255, 255))
        cv2.putText(bframe1, '2.2 Smoothing or Blurring', (10, height - 200), font, 1, (255, 255, 255))
        # add_two frames
        added_image1 = np.concatenate((gframe1, bframe1), axis=0)
        out1.write(added_image1)
    elif f > 140 and f <= 220:
        ksize = 81
        gframe1 = cv2.GaussianBlur(frame, (ksize, ksize), 0)
        cv2.putText(gframe1, 'Gaussian filters', (10, 30), font, 0.5, (255, 255, 255))
        cv2.putText(gframe1, 'ksize = 81', (10, 50), font, 0.5, (255, 255, 255))
        cv2.putText(gframe1, 'Gaussian-processed img getting more fuzzy', (10, 70), font, 0.5, (255, 255, 255))
        cv2.putText(gframe1, 'because the Gaussian filter only considers spatial proximity', (10, 90), font, 0.5, (255, 255, 255))
        # Apply bilateral filter
        bframe1 = cv2.bilateralFilter(frame, ksize, 75, 75)
        cv2.putText(bframe1, 'Bilateral filters', (10, height-30), font, 0.5, (255, 255, 255))
        cv2.putText(bframe1, 'ksize = 81', (10, height-50), font, 0.5, (255, 255, 255))
        cv2.putText(bframe1, 'Bilateral-processed img is still very clear', (10, height - 70), font, 0.5, (255, 255, 255))
        cv2.putText(bframe1, 'Because bilateral filter takes into account both spatial proximity and pixel intensity similarity', (10, height - 90), font, 0.2, (255, 255, 255))
        cv2.putText(bframe1, '2.2 Smoothing or Blurring', (10, height - 200), font, 1, (255, 255, 255))
        # add_two frames
        added_image1 = np.concatenate((gframe1, bframe1), axis=0)
        print(added_image1.shape)
        out1.write(added_image1)
    cv2.imshow('Edges', added_image1)
    if cv2.waitKey(1) == 27:
        break





"""
1. upper: Gaussisian filter， lower is : bi-lateral filters
2. 每一秒：ksize分别是11，31，,41，51，,61，,71，81,用cv2.puttext表示一下
3.  When kener size increases, bilateral is more clear than Gaussian filters
Because bilateral filter takes into account both spatial proximity and pixel intensity similarity, 
whereas the Gaussian filter only considers spatial proximity. 
Therefore, the bilateral filter is more effective in smoothing images while preserving edges and details
"""








