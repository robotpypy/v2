# -*- coding: utf-8 -*-
"""
Created on Sat Jun 29 01:06:41 2019

@author: Amanda
"""

import cv2
import time
import numpy as np
from face_det import face_det
from color_det import Color
from Get_distance import distance

if __name__ == '__main__':
    
    # ---- Camera   
    #vidcap = cv2.VideoCapture('test_video.mp4')    
    #count = 0
    
    
    
    #while True:
        
    # ---- Read the image
    
    '''
    (success, image)= vidcap.read()
    name = 'frame' + str(count) + '.jpg'
    print ('Creating...' + name)         
    count += 1                
    '''
            
    image_path = 'test.png'
    image = cv2.imread(image_path, cv2.IMREAD_UNCHANGED)            
        
    # ---- Face detection
    (N_face, face_pos, image_face) = face_det(image)
    print("detect", N_face, "features.")
    print("position of the features:", face_pos)
    
    # ---- Color detection
    IP_color = Color() # class Color
    (image_mask, color_pos) = IP_color.color_det(image)     
    
    # --- show images
    '''
    image_ = cv2.resize(image, (0,0), fx=0.5, fy=0.5) 
    image_face_ = cv2.resize(image_face, (0,0), fx=0.5, fy=0.5) 
    image_mask_ = cv2.resize(image_mask, (0,0), fx=0.5, fy=0.5) 
    cv2.imshow("image1", np.hstack([image_, image_face_]))
    cv2.imshow("image2", np.hstack([image_, image_mask_]))
    #cv2.waitKey(0)
    if cv2.waitKey(1) == 27:  # press ESC in to close all shown images     
        cv2.destroyAllWindows()               
        break
    '''
    
    # --- Sensir fusion or linear model
    
    # Table 1 (horizontal)
    # Table 2 (vertical)
          
    table = { "orientation": 60,\
              "cor_x": face_pos[0][0] ,\
              "cor_y": face_pos[0][1]}

    coordination = distance(table)
    land_x, land_y = coordination.distance_to_landmark()
    print(land_x, land_y)   
    
    # --- RL  
    
    
    
    # --- Timer
    #time.sleep(1) # delay 10 seconds


    # end while
        
    
    
    #vidcap.release()
    #out.release()
    