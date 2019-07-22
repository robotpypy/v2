# -*- coding: utf-8 -*-
"""
Created on Mon Jul  1 14:36:13 2019

@author: Amanda
"""
import cv2
import numpy as np

def face_det(image):    
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    
#    # Read the image
#    image_path = 'grass_4.png'
#    image = cv2.imread(image_path, cv2.IMREAD_UNCHANGED)
#    
#    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Detect faces in the image
    faces = face_cascade.detectMultiScale(
        image,
        scaleFactor=1.25,#1.25,
        minNeighbors=2,
        minSize=(30, 30),
    )
    #print(faces)
    N_face = len(faces)
    #print('Found {0} faces!'.format(len(faces)))
    
    # Draw a rectangle around the faces
    image_ = np.copy(image)
    for (x, y, w, h) in faces:
        cv2.rectangle(image_, (x, y), (x + w, y + h), (0, 255, 0), 2)

        
    #cv2.imshow("Faces found", image)
    cv2.imwrite("[Output]face_det.jpg", image_)
    #cv2.waitKey(0)
        
    #cv2.destroyAllWindows()

    return N_face, faces, image_
    
    
    
if __name__ == '__main__':
    image_path = 'test.png'
    image = cv2.imread(image_path, cv2.IMREAD_UNCHANGED)    
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    N_face, faces = face_det(gray)