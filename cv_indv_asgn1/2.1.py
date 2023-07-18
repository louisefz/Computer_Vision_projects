import cv2
import numpy as np
# reading the video
source = cv2.VideoCapture('/Users/zhoujie/Desktop/video/1.mp4')
fps = 35   #帧率要在40.5才能完成4s的时长
size = (int(source.get(cv2.CAP_PROP_FRAME_WIDTH)),
        int(source.get(cv2.CAP_PROP_FRAME_HEIGHT)))
frame_count = int(source.get(cv2.CAP_PROP_FRAME_COUNT))
print(size)
print(frame_count)
# certain frame frame info
height = int(source.get(4))


out_video_dir = '/Users/zhoujie/Desktop/video/1_out.mp4'



out = cv2.VideoWriter(out_video_dir,cv2.VideoWriter_fourcc(*'mp4v'), fps, size)

font = cv2.FONT_HERSHEY_SIMPLEX
dict_img = {1: range(20), 2: range(20,40), 3: range(40,60), 4: range(60,80), 5: range(80,110),6:range(110,140)}
# dict_img = {range(30):1, range(30,60):2, range(60,90):3, range(90,120):4, range(120,163):5}
img_array = []
for k, v in dict_img.items():
    if k%2 == 1:
        for i in v:
            source.set(cv2.CAP_PROP_POS_FRAMES,i)
            _, img = source.read()
            cv2.putText(img, 'coloured frames', (10, height - 30), font, 0.5, (255, 255, 255))
            cv2.putText(img, '2.1 color and grayscale', (10, height - 70), font, 1, (255, 255, 255))

            # cv2.imshow('Video Player', img)
            img_array.append(img)

    elif k%2 == 0:
        for i in v:
            source.set(cv2.CAP_PROP_POS_FRAMES,i)
            _, img2 = source.read()
            gray_img = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

            img3 = cv2.merge((gray_img, gray_img, gray_img))  # 1 channe into 3 channels
            cv2.putText(img3, 'gray frames: cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)', (10, height - 30), font, 0.5, (255, 255, 255))
            cv2.putText(img3, '2.1 color and grayscale', (10, height - 70), font, 1, (255, 255, 255))

            # cv2.waitKey()
            img_array.append(img3)
            # cv2.destroyAllWindows()
for i in range(len(img_array)):
    out.write(img_array[i])





"""
cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY) is used to convert colour frames into black ones in some periods

"""












