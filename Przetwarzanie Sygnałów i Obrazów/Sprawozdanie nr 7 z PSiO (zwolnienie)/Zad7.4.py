import mahotas
from pylab import imshow, show
import cv2

img = mahotas.imread('livingroom.tif')

imshow(img)
show()

img = mahotas.thresholding.bernsen(img, 5, 100)

imshow(img)
show()
