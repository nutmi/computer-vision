
import pygetwindow
import cv2 as cv 
import numpy as np
from PIL import ImageGrab
import win32gui

def window_capture():

    hwnd = win32gui.FindWindow(None, r'Albion Online Client')
    win32gui.SetForegroundWindow(hwnd)
    dimensions = win32gui.GetWindowRect(hwnd)

    image = ImageGrab.grab(dimensions)
    image = np.array(image)
    image = cv.cvtColor(image, cv.COLOR_RGB2BGR)
    return image

print(pygetwindow.getAllTitles())