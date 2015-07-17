import numpy as np
import cv2

def resizeImg(img):
	dst = cv2.resize(img, None, fx=0.30, fy=0.30, interpolation = cv2.INTER_LINEAR)
	return dst

face_cascade = cv2.CascadeClassifier("/home/pi/EyeInThePi/opencv-2.4.9/data/haarcascades/haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier("/home/pi/EyeInThePi/opencv-2.4.9/data/haarcascades/haarcascade_mcs_lefteye.xml")
mouth_cascade = cv2.CascadeClassifier("/home/pi/EyeInThePi/opencv-2.4.9/data/haarcascades/haarcascade_mcs_mouth.xml")
nose_cascade = cv2.CascadeClassifier("/home/pi/EyeInThePi/opencv-2.4.9/data/haarcascades/haarcascade_mcs_nose.xml")
#these classifiers are needed for the program to run

path = "/home/pi/EyeInThePi/"
img = cv2.imread(path + "greyScale.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray, 1.3, 5)
#eyes = eye_cascade.detectMultiScale(gray)
for (x, y, w, h) in faces:
	cv2.rectangle(img, (x, y), (x+w, y+w), (0, 255, 0), 2)
	roi_gray = gray[y:y+h, x:x+w]
	roi_color = img[y:y+h, x:x+w]
eyes = eye_cascade.detectMultiScale(roi_gray)
	
for (ex, ey, ew, eh) in eyes:
	cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (255, 255, 0), 2)
	mouth = mouth_cascade.detectMultiScale(roi_gray)
	for (mx, my, mw, mh) in mouth:
		cv2.rectangle(roi_color, (mx, my), (mx+mw, my+mh), (0, 255, 255), 2) 
		
	nose = nose_cascade.detectMultiScale(roi_gray)
	for (nx, ny, nw, nh) in nose:
		cv2.rectangle(roi_color, (nx, ny), (nx+nw, ny+nh), (255, 255, 0), 2) 


cv2.imwrite("leftEye.png", img)
cv2.imshow("img", img)
cv2.imshow("gray", gray)
cv2.waitKey(0)
cv2.destroyAllWindows()
