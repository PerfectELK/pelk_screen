import ctypes
from numpy.ctypeslib import ndpointer
import numpy as np

screen = ctypes.cdll.LoadLibrary('./screenlib.so')

width = screen.getWidth()
height = screen.getHeight()
colors = 3

def getScreenShot():
    array = np.array(screen.getScreenShot())
    array = array.reshape((height, width, colors))
    return array

screen.getScreenShot.restype = ndpointer(dtype=ctypes.c_int32, shape=(width * height * 3))