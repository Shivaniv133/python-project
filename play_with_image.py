import cv2
print("imported....")
from PIL import Image
image = Image.open("./shinchan.jpeg")
image = cv2.imread("./shinchan.jpeg")
gray_image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
cv2.rectangle (image, (100,100),(250,250),(123,123,123),3)
while True:
    cv2.imShow("This is my first image",image)
    cv2.imShow("This is my GRAY image",gray_image)
    if cv2.waitKey(1) == ord("q"):
        break 
image.show()

import cv2
import cv2.data
modelPath = cv2.data.haarcascades + "/haarcascade_frontalface_default.xml"
model=cv2.CascadeClassifier(modelPath)
cam = cv2.VideoCapture(0)
while True:
    status,image =  cam.read()
    faces = model.detectMultiScale(image,1.3,5)
    for face in faces:
        x = face[0]
        y = face[1]
        w = face[2]
        h = face[3]
        cv2.rectangle(image,(x,y),(x+w,y+h),(0 ,0 ,255),2)
    cv2.imshow("Face",image)
    if cv2.waitKey(1) == ord("q"):
        break
        
