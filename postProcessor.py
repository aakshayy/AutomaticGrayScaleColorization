import cv2

def postProcess(img):
	median = cv2.median(img)
	return median