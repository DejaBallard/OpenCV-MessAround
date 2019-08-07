import numpy as np
import cv2
import random as r

img = cv2.imread("fuzzy.png",1)

#change to gray scale to be able to threshold
gray = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
blur = cv2.GaussianBlur(gray,(3,3),0)

adapt = cv2.adaptiveThreshold(blur,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,205,1)
_, contour, heirarchy = cv2.findContours(adapt,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

filtered = []
for c in contour:
    # if the c area is less than 1000, skip / continue to the next c in contour
    if cv2.contourArea(c) < 1000: continue
    # add this c to the filtered array
    filtered.append(c)
num = 0
objects = np.zeros([img.shape[0],img.shape[1],3], 'uint8')

for c in filtered:
    # get a random color
    col = (r.randint(0,255),r.randint(0,255),r.randint(0,255))
    # draw the contour on objects, it being filled
    cv2.drawContours(objects,[c],-1,col,-1)
    # get the area
    area = cv2.contourArea(c)
    # get the preminitor, true means it is a closed arch
    p = cv2.arcLength(c,True)
    # count how many objects there is
    num = num + 1
    print( area, p, num, col)

cv2.imshow("ori",img)
cv2.imshow("gray",gray)
cv2.imshow("bur",blur)
cv2.imshow("adapt",adapt)
cv2.imshow("t",objects)
cv2.waitKey(0)
cv2.destroyAllWindows()