import cv2

def postProcess(img):
	median = cv2.medianBlur(img,5)
	return median