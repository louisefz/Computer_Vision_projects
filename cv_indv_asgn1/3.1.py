import cv2
import numpy as np
import random



# Load the image
img = cv2.VideoCapture('/Users/zhoujie/Desktop/video/4.mp4')


frame_width = int(img.get(3))
frame_height = int(img.get(4))
size = (frame_width, frame_height*2)
print(size)
font = cv2.FONT_HERSHEY_SIMPLEX

out = cv2.VideoWriter('/Users/zhoujie/Desktop/video/4_out.mp4',
                         cv2.VideoWriter_fourcc(*'mp4v'),25,size)
while True:
    # Read a frame from the video file
    ret, frame = img.read()

    if not ret:
        # End of video file
        break
    # Convert to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Define the range of values for the Sobel parameters
    ksize = random.randrange(3, 31, 2)
    scale = random.choice(np.linspace(0.1, 1, 10))
    delta = random.randrange(0, 51, 5)

    # Set the number of iterations and samples for random search
    num_iterations = 100
    # num_samples = 5

    # Initialize the best parameters and score
    best_params = None
    best_score = 0


    # Apply the Sobel operator
    sobelx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=ksize, scale=scale, delta=delta)
    sobely = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=ksize, scale=scale, delta=delta)

    # Compute the edge image
    edges = cv2.addWeighted(sobelx, 0.5, sobely, 0.5, 0)

    # Compute the score (e.g. number of nonzero pixels in the edge image)
    score = np.count_nonzero(edges) / (edges.shape[0] * edges.shape[1])

    # Update the best parameters and score if the current score is better
    if score > best_score:
        best_params = (ksize, scale, delta)
        best_score = score

    # Apply the color map to the edges
    edges_color = cv2.applyColorMap(cv2.convertScaleAbs(edges), 6)
    concat_img = np.concatenate((frame, edges_color), axis=0)
    cv2.putText(concat_img, 'use sobel edge detection: cv2.sobel()', (10, 10), font, 0.4, (255, 255, 255))
    cv2.putText(concat_img, 'best_ksize: 11 from random.randrange(3, 31, 2)', (10, 30), font, 0.4, (255, 255, 255))
    cv2.putText(concat_img, 'best_scale: 0.9 from random.choice(np.linspace(0.1, 1, 10))', (10, 50), font, 0.4, (255, 255, 255))
    cv2.putText(concat_img, 'best_delta: 0 from random.randrange(0, 51, 5)', (10, 70), font, 0.4, (255, 255, 255))
    cv2.putText(concat_img, 'use colour 6: COLORMAP_SUMMER ', (10, 90), font, 0.4, (255, 255, 255))
    cv2.putText(concat_img, '3.1 Sobel edge detection', (10, 140), font, 1, (255, 255, 255))
    print(concat_img.shape)

    out.write(concat_img)
    # Show the colorized edges and wait for a key press
    cv2.imshow('Edges', concat_img)
    if cv2.waitKey(1) == 27:
        break

        # Visualize the edges for 1 second
        # cv2.imshow('Edges', edges)
        # cv2.waitKey(1000)

# Print the best parameters and score
print('Best parameters:', best_params)
print('Best score:', best_score)


###
# Best parameters: (11, 0.9, 0)
# Best score: 0.9999830163043478

"""
1. turn the coloured frames into gray ones
2. sobel edge detection: cv2.sobel()
3. parameters (ksize, scale, delta) changes on every frame
4. best paramater is (11, 0.9, 0), Best score: 0.9999830163043478
5. apply colour: cv2.applyColorMap(cv2.convertScaleAbs(edges), 6), 
6. colour 6: COLORMAP_SUMMER 

"""