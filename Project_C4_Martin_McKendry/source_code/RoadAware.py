#!/usr/bin/env Python 

# All of the imports used
import cv2
import math
import time
import pygame
from picamera.array import PiRGBArray
from picamera import PiCamera
import numpy as np

#Definition of the classifiers and their locations 
face_cascade = cv2.CascadeClassifier("/home/pi/EyeInThePi/opencv-2.4.9/data/haarcascades/haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier("/home/pi/EyeInThePi/opencv-2.4.9/data/haarcascades/haarcascade_mcs_righteye.xml")

#These are used for playing the sound
pygame.mixer.init()
pygame.mixer.music.load("/home/pi/Downloads/beep.mp3")

#Initialising the camera, defining resolution and framerate
camera = PiCamera()
camera.resolution = (150, 150)
camera.framerate = 24
rawCapture = PiRGBArray(camera, size=(150, 150))
time.sleep(0)

#The frames variable is the counter and the maxFrames is the threshold before the alert goes off
frames = 0
maxFrames = 10



#reduces the size of the image for faster processing
def shrinkImg(img):
	dst = cv2.resize(img, None, fx=0.80, fy=0.80, interpolation = cv2.INTER_LINEAR)
	return dst
#enlarges image for clearer display
def enlargeImg(img):
	dst = cv2.resize(img, None, fx=2.00, fy=2.00, interpolation = cv2.INTER_LINEAR)
	return dst

#Function for facial detection and eye tracking
def detectFace(image):
	#iterate through and draw a bounding box over face
	for (x, y, w, h) in faces:
		cv2.rectangle(image, (x, y), (x+w, y+w), (255, 0, 0), 2) 
		roi_color = image[y:y+h, x:x+w]
		
		#take the face and make it the region of interest
		roi = image[y:y+h, x:x+w]
		#crop the region of interest to the right eye 
		#limits search window of the right eye
		cropped = roi[10:80, 30:100]
		cv2.imshow("Eye", cropped)
		
		#Detect eye in the new cropped window
		eye = eye_cascade.detectMultiScale(cropped, 1.3, 5)
		for (x, y, w, h) in eye:
			#iterate through and draw bounding box
			cv2.rectangle(cropped, (x, y), (x+w, y+w), (0, 0, 155), 2) 
			roi_color = cropped[y:y+h, x:x+w]
			#if eye is found reset the count and return it
			if(eye is not None and len(eye) > 0):
				frames = 0
				
	return image


# This loops takes a video feed and pulls out each frame and analyzes it
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
		
	image = frame.array
	image = shrinkImg(image)
	#converting the image to grey scale to apply classifiers
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	
	#Apply the face classifier to the image
	faces = face_cascade.detectMultiScale(gray, 1.3, 5)
		
	
	
	#If there is an face detected reset the frame counter
	if(faces is not None and len(faces) > 0):
		#frames = 0
		frames += frames
		detectFace(image)
		
	#Else add to frames, if the count reaches the max count then sound alert 	
	else:
		frames += 1
		if (frames == maxFrames):
			pygame.mixer.music.play()
			frames = 0
		print frames
		
	resImage = enlargeImg(image)
	#display the image (for testing and demonstration)
	cv2.imshow("image", resImage) 
	
	#waiting to detect key press
	key = cv2.waitKey(1) & 0xFF
		
		
	rawCapture.truncate(0)
	
	#Loop plays until the 'q' key is pressed	
	if key == ord("q"):
		break

