
import os
import cv2
import math
import time
import picamera

def resizeImg(img):
	dst = cv2.resize(img, None, fx=0.30, fy=0.30, interpolation = cv2.INTER_LINEAR)
	return dst


#taking a picture using the pi camera
with picamera.PiCamera() as camera:
	camera.resolution = (640, 400)
	camera.start_preview()
	
	time.sleep(10)
	camera.capture('foo.jpg')
	
#os.system("raspistill -vf -o test.jpg")

path = "/home/pi/EyeInThePi/"

#loading the image
img = cv2.imread(path + "foo.jpg")
grey = cv2.imread(path + "foo.jpg", 0) #the 0 is for greyscale


#resize image
#img = resizeImg(img)
#grey = resizeImg(grey)

cv2.imwrite(path + "greyScale.jpg", grey)
cv2.imwrite(path + "imagecolor.jpg", img)

#display images

cv2.imshow("img", img)
cv2.imshow("greyScale", grey)


cv2.waitKey(0)
