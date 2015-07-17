#!/usr/bin/env Python
import numpy as np
import cv2
import math
import time
import picamera
from PIL import Image

with picamera.PiCamera() as camera:
	camera.resolution = (400, 400)
	camera.start_preview()
	time.sleep(0.5)
	try:
		for i, filename in enumerate(camera.capture_continuous('img{counter}.jpeg')):
			print('captured %s' % filename)
			time.sleep(0.5)
			camera.annotate_text = "Live"
			img = Image.open(filename) 
			if i == 9:
				
				break
	finally:
		camera.stop_preview()
		
