import numpy as np
import cv2

# haar cascade method
# feature based machine learning
# uses pretrained images of labeled positives and negatives
# runs via thousands of classidisers in a cascade manner


img = cv2.imread("faces.jpeg",1)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

path = "haarcascade_frontalface_default.xml"

#loads the xml
face_cascade = cv2.CascadeClassifier(path)

faces = face_cascade.detectMultiScale(gray,scaleFactor=1.05,minNeighbors=6,minSize=(40,40))

print(len(faces))

for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)

cv2.imshow("imge",img)

cv2.waitKey(0)