import cv2
import os
def createFolderTest(imagesPath,resize=True):
	basePath = "./"
	newPath = getAndCreateNextFolder(basePath)
	for imagePath in imagesPath:
		dumpImage(newPath,imagePath,imagesPath.index(imagePath)+1,resize)

def dumpImage(newPath,imagePath,index,resize):
	image = cv2.imread(imagePath)
	imageGray = cv2.imread(imagePath,0)
	if resize == True:
		image = resizeImage(image)
		imageGray = resizeImage(imageGray)
	savePath = newPath+str(index)+".jpg"
	savePathGray = newPath+str(index)+"G.jpg"
	print cv2.imwrite(savePath,image)
	print cv2.imwrite(savePathGray,imageGray)

def getAndCreateNextFolder(basePath):
	folderNumber = 1
	while 1:
		newPath = basePath + str(folderNumber) + "/"
		try:
			os.stat(newPath)
			folderNumber = folderNumber + 1
		except:
			os.mkdir(newPath)
			return newPath

def resizeImage(image):
	m = image.shape[0]
	n = image.shape[1]
	maxPixelSize = 400
	resizeFactor1 = (float)(1)/((float)(m)/maxPixelSize)
	resizeFactor2 = (float)(1)/((float)(n)/maxPixelSize)
	resizeFactor = min(resizeFactor1,resizeFactor2)
	if resizeFactor >= 1:
		return image
	return cv2.resize(image,(0,0),fx=resizeFactor,fy=resizeFactor)

if __name__ == "__main__":
	pass
	#createFolderTest(["./temp/mountain1.jpeg","./temp/mountain2.jpeg"])
	#createFolderTest(["./temp/abc.jpg"])