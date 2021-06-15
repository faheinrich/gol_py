import numpy as np
import scipy.signal
import cv2

heigth = 500
width = 500
cells = np.uint8(np.random.binomial(n=1, p=0.5, size=[heigth, width]))
conv_filter = np.array([[1,1,1],[1,0,1],[1,1,1]])

while(1):
    cv2.imshow("gol", cv2.resize(cells * 255, (width*1, heigth*1)))
    cv2.waitKey(1)
    neighbour_count = scipy.signal.convolve2d(cells, conv_filter, mode='same')
    cells &= (neighbour_count == 2)
    cells |= (neighbour_count == 3)
