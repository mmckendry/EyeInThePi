import cv2
import math
import time
import picamera

img = "foo.jpg"
with picamera.PiCamera() as camera:
	camera.resolution = (400, 400)
	camera.start_preview()
	time.sleep(2)
	for i in range (0, 10):
		camera.capture(img)	
		img = str(i) + (img) 

#cv2.imshow("img", img)
