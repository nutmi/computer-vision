import cv2 as cv
import numpy as np


def findclickposition(image, threshold=0.5):
    limestone_img = cv.imread('albion_limestone.jpg', cv.IMREAD_UNCHANGED)
    
    limestone_w = limestone_img.shape[1]
    limestone_h = limestone_img.shape[0]

    method = cv.TM_CCOEFF_NORMED

    result = (image, limestone_img, method)

    locations = np.where(result >= threshold)
    locations = list(zip(*locations[::-1]))

    rectangles = []

    for loc in locations:
        rec = [int(loc[0]), int(loc[1], limestone_w, limestone_h)]

        rectangles.append(rec)
        rectangles.append(rec)

    rectangles, weights = cv.groupRectangles(rectangles, groupThreshold=1, eps=0.5)

    points = []

    if len(rectangles):

        line_color = (0, 255, 0)
        line_type = cv.LINE_4
        marker_color = (255 ,0 ,255)
        market_type = cv.MARKER_CROSS

        for (x, y, w, h) in rectangles:

            center_x = x + int(w/2)
            center_y = y + int(h/2)
            

