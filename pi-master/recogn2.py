#!/usr/bin/python

# Import the required modules
import cv2, os
import numpy as np
from PIL import Image

# For face detection we will use the Haar Cascade provided by OpenCV.
cascadePath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath)

# For face recognition we will the the LBPH Face Recognizer 
recognizer = cv2.face.createLBPHFaceRecognizer()
recognizer.load('model.xml')

path = './thirdeye'
# Append the images with the extension .sad into image_paths
#image_paths = [os.path.join(path, f) for f in os.listdir(path) if f.endswith('.sad')]


predict_image_pil = Image.open("face.jpg").convert('L')
predict_image = np.array(predict_image_pil, 'uint8')
faces = faceCascade.detectMultiScale(predict_image)
#print(len(faces))
for (x, y, w, h) in faces:
    if((h<400) | (w<400)):
       continue
    nbr_predicted,conf = recognizer.predict(predict_image[y: y + h, x: x + w])
    print nbr_predicted
    if(nbr_predicted==1):
	nbr_actual="bala"
    elif(nbr_predicted==2):
	nbr_actual="neha"
    elif(nbr_predicted==3):
	nbr_actual="deepika"
    else:
	nbr_actual="prash"
    """
    nbr_actual1 = (os.path.split(image_path)[1].split(".")[0])#.replace("subject", ""))
    
    if nbr_actual == nbr_predicted:
    """
    print nbr_actual, "is recognized with a confidence measure of" ,conf
    """else:
    #    print "{} is Incorrect Recognized as {}".format(nbr_actual, nbr_predicted)
    """    
    cv2.imshow("Recognizing Face", predict_image[y: y + h, x: x + w])
    cv2.waitKey(1000)
