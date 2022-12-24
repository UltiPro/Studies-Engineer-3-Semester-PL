import cv2

appleb = cv2.imread('apple b.png',cv2.IMREAD_COLOR)
appleg = cv2.imread('apple g.png',cv2.IMREAD_COLOR)
appler = cv2.imread('apple r.png',cv2.IMREAD_COLOR)

appleb = cv2.flip(appleb,1)

appleg = cv2.rotate(appleg,cv2.cv2.ROTATE_180)

apple = appleb + appleg + appler

apple = cv2.dilate(apple, cv2.getStructuringElement(cv2.MORPH_RECT, (1,1)), iterations = 1)
mask = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))
apple = cv2.morphologyEx(apple,cv2.MORPH_CLOSE, mask)

cv2.imwrite('apple.png',apple)