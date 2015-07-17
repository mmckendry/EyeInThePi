#!/usr/bin/env Python
import numpy as np
import cv2
import cv2.cv
import math
import time
import picamera
from PIL import Image
def resizeImg(img):
	dst = cv2.resize(img, None, fx=1.0, fy=1.0, interpolation = cv2.INTER_LINEAR)
	return dst

face_cascade = cv2.CascadeClassifier("/home/pi/EyeInThePi/opencv-2.4.9/data/haarcascades/haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier("/home/pi/EyeInThePi/opencv-2.4.9/data/haarcascades/haarcascade_mcs_lefteye.xml")

path = "/home/pi/EyeInThePi/"
img = cv2.imread(path + "foo.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = resizeImg(gray)
face = face_cascade.detectMultiScale(gray, 1.3, 5)

for (x, y, w, h) in face:
	cv2.rectangle(img, (x, y), (x+w, y+w), (0, 255, 155), 2)
	roi_color = img[y:y+h, x:x+w]
	roi = img[y:y+h, x:x+w]
	

cropped = roi[10:120, 20:90]
eye = eye_cascade.detectMultiScale(cropped, 1.3, 5)
for (x, y, w, h) in eye:
	cv2.rectangle(cropped, (x, y), (x+w, y+w), (0, 0, 155), 2)
	roi_cropped = cropped[y:y+h, x:x+w]
	
cv2.imshow("blownUpImg.jpg", roi)
#cv2.imshow("wreked.jpg", img)
cv2.imshow("cropped",cropped)
cv2.waitKey(0)
cv2.destroyAllWindows()
