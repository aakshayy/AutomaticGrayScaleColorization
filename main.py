import cv2
import numpy
from quant import quantization 
from getKeyPointFeatures import getKeyPointFeatures
from training import train
from prediction import predict
from sklearn.decomposition import PCA
from sklearn import preprocessing
from postProcessor import postProcess
if __name__=="__main__":
	t1 = cv2.getTickCount()
	
	#Defining constants
	trainingImagePath = "./Images/3/1.jpg"
	grayscaleImagePath = "./Images/3/1G.jpg"
	outputImagePath = "./Images/3/output.jpg"
	#trainingImagePath = "../Trad Database/col.jpg"
	#grayscaleImagePath = "../Trad Database/bw2.jpg"
	k = 5

	#Reading Training Image
	trainingImage = cv2.imread(trainingImagePath)
	trainingImage = cv2.cvtColor(trainingImage,cv2.COLOR_BGR2LAB)
	m,n,_ = trainingImage.shape

	#Preprocessing variable from image
	l = trainingImage[:,:,0]
	a = trainingImage[:,:,1]
	b = trainingImage[:,:,2]
	
	scaler = preprocessing.MinMaxScaler()
	pca = PCA(32)

	qab,centroid = quantization(a,b,k)
	print centroid
	t2 = cv2.getTickCount()
	t = (t2 - t1)/cv2.getTickFrequency()
	print "Time for quantization : ",t," seconds"
	

	feat,classes = getKeyPointFeatures(l,qab)
	feat = scaler.fit_transform(feat)
	feat = pca.fit_transform(feat)

	
	t3 = cv2.getTickCount()
	t = (t3 - t2)/cv2.getTickFrequency()
	print "Time for feature extraction : ",t," seconds"
	
	
	svm_classifier = train(feat,classes,k)
	t4 = cv2.getTickCount()
	t = (t4 - t3)/cv2.getTickFrequency()
	print "Time for training: ",t," seconds"

	grayscaleImage = cv2.imread(grayscaleImagePath,0)
	outputTempImage = predict(svm_classifier,grayscaleImage,centroid,scaler,pca)
	outputImage = postProcessing(outputTempImage) 
	t5 = cv2.getTickCount()
	t = (t5 - t4)/cv2.getTickFrequency()
	print "Time for prediction : ",t," seconds"	
	t = (t5 - t1)/cv2.getTickFrequency()
	print "Total time : ",t," seconds"
	outputImage = cv2.cvtColor(outputImage,cv2.COLOR_LAB2BGR)
	trainingImage = cv2.cvtColor(trainingImage,cv2.COLOR_LAB2BGR)
	cv2.imwrite(outputImagePath,outputImage)
	cv2.imshow("Predicted",outputImage)
	cv2.imshow("Training",trainingImage)
	cv2.imshow("Original",grayscaleImage)
	cv2.waitKey()
	cv2.destroyAllWindows()
