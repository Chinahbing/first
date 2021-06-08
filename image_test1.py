import cv2
import numpy as np
from PIL import Image

img1 = cv2.imread('images/01.jpg')
cv2.namedWindow('01', cv2.WINDOW_NORMAL)
cv2.imshow('01', img1)
print(img1.shape)
hight, width = img1.shape[0:2]
img2 = cv2.resize(img1,(width,hight))
cv2.imshow('02', img2)

cv2.waitKey(0)
cv2.destroyAllWindows()

# img2 = Image.open('images/02.jpg')
# print(img2.size)
# print(img2.mode)
# print(type(img2))
# img2.show()