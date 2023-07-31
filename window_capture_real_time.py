import cv2 as cv
import numpy as np
import pygetwindow
import pyautogui
from time import time
from all_titles import window_capture

loop_time = time()
while True:
    screenshot = window_capture()

    cv.imshow('screenshot', screenshot)
    print('fps {}'.format ( 1 / (time() - loop_time)))
    loop_time = time()

    if cv.waitKey(1) == ord('q'):
        break
cv.destroyAllWindows()
print('done')
window_capture()