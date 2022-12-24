import cv2
import numpy as np

src = cv2.imread('obrazek.png', cv2.IMREAD_UNCHANGED)
dst = cv2.GaussianBlur(src, (3, 3), cv2.BORDER_DEFAULT)

kernel = np.array([[-1,-1,-1], 
                    [-1, 9,-1],
                    [-1,-1,-1]])
sharpened = cv2.filter2D(src, -1, kernel) 
cv2.imshow('Image Sharpening',np.hstack((src, sharpened)))

cv2.imshow("Gaussian Smoothing", np.hstack((src, dst)))
cv2.waitKey(0)
cv2.destroyAllWindows()