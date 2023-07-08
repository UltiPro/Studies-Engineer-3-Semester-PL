import cv2

image = cv2.imread('cameraman.tif')

image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

ret, otsu = cv2.threshold(image, 120, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

cv2.imwrite('otsu_cameraman.png', otsu)
