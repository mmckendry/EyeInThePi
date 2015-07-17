import numpy as np
import cv2
import math
import time
import picamera

name = "w.png"
path = "/home/pi/EyeInThePi/pictures/"
with picamera.PiCamera() as camera:
	camera.resolution = (400, 400)
	camera.start_preview()
	time.sleep(0.5)
	for i in range (0, 11):
		camera.capture(path + name)	
		name = str(i) + (name) 
	
		#img = camera.capture('pictures/w.png')
	
	


img = cv2.imread(path + name)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


cv2.imshow("img", img)
cv2.imshow("gray", gray)
cv2.waitKey(0)
cv2.destroyAllWindows()
