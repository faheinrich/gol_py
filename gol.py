import numpy as np
import scipy.signal
import cv2

def main():
    heigth = 500
    width = 500
    cells = np.uint8(np.random.binomial(n=1, p=0.5, size=[heigth, width]))
    conv_filter = np.array([[1,1,1],[1,0,1],[1,1,1]])
    pause_time = 100 # 100 = 100ms

    while(1):
        cv2.imshow("gol", cv2.resize(cells * 255, (width*1, heigth*1)))
        if cv2.waitKey(pause_time) & 0xFF == 27:
            break
        neighbour_count = scipy.signal.convolve2d(cells, conv_filter, mode='same')
        cells &= (neighbour_count == 2)
        cells |= (neighbour_count == 3)


if __name__ == "__main__":
    main()