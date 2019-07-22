# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 19:24:12 2019

@author: Amanda
"""

'''
https://www.pyimagesearch.com/2014/08/04/opencv-python-color-detection/
'''

# import the necessary packages
import numpy as np
#import argparse
import cv2
#from PIL import Image
#from matplotlib import pyplot as plt

 
 
# construct the argument parse and parse the arguments
#ap = argparse.ArgumentParser()
#ap.add_argument("-i", "--image", help = "path to the image")
#args = vars(ap.parse_args())
 
# load the image
#image = cv2.imread(args["image"])

#img = Image.open('grass_4.png')
#print("initial size",img.size)
#img1 = img.resize((128, 128))

#image = cv2.imread('grass_4.png', cv2.IMREAD_UNCHANGED)

# --- global variables



class Color:    
    def __init__(self): 
        self.W_RES = 45
        self.H_RES = 60
        self.TRD = 255 * 10  # threshold
        
    def color_det(self, image):    
        # --- get boundary value
        img=np.array(image)
        ##print(img.ndim, img.shape)
        #
        #red_fla = img[:,:,0].flatten()
        #red_mean = np.mean(red_fla)
        #red_std = np.std(red_fla)
        #
        #gre_fla = img[:,:,1].flatten()
        #gre_mean = np.mean(gre_fla)
        #gre_std = np.std(gre_fla)
        #
        #blue_fla = img[:,:,2].flatten()
        #blue_mean = np.mean(blue_fla)
        #blue_std = np.std(blue_fla)
        #
        #print([red_mean - red_std, gre_mean - gre_std, blue_mean - blue_std],
        #      [red_mean + red_std, gre_mean + 2*gre_std, blue_mean + blue_std],
        #      [red_mean - 2*red_std, gre_mean - 2*gre_std, blue_mean - 2*blue_std],
        #      [red_mean + 2*red_std, gre_mean + 2*gre_std, blue_mean + 2*blue_std],
        #)
        # (end) get boundary value
        
        #height = np.size(image, 0)
        #width = np.size(image, 1)
        #print('iamge size: ', height, width)
        
        #res=cv2.resize(image, (height / 2, width / 2), interpolation=cv2.INTER_LINEAR)
        #cv2.imshow('image1', image) # '...': name of the shown figure
         
        
        
        blank_image2 = 255 * np.ones(img.shape, dtype=np.uint8)
        #cv2.imwrite("white_blank.png", blank_image2)
         
         
        
        # --- define the list of boundaries
        # black: rgb(0,0,0)
        boundaries = [
                
            #([17, 15, 100], [50, 56, 200]),
            #([86, 31, 4], [220, 88, 50]),
            #([25, 146, 190], [62, 174, 250]),
            #([103, 86, 65], [145, 133, 128]),
            ([90, 160, 130], [130, 220, 190]), # green
            #([51, 99, 73], [106, 183, 130]),
            #([24, 71, 45], [133, 183, 159]),
        ]
        
        # loop over the boundaries
        for (lower, upper) in boundaries:
        
            #print((lower, upper))
            # create NumPy arrays from the boundaries
            lower = np.array(lower, dtype = "uint8")
            upper = np.array(upper, dtype = "uint8")
            
            # find the colors within the specified boundaries and apply
            # the mask
            mask = cv2.inRange(image, lower, upper)
            #output = cv2.bitwise_and(image, image, mask = mask)
            image_mask = cv2.bitwise_and(blank_image2, blank_image2, mask = mask)
            
            out = self.grid_det(image_mask)
            #print(out)
            
            #--- show the images
            #cv2.imshow("image", np.hstack([image, mask_image]))
            #cv2.waitKey(0)
         
            # save 
            #cv2.imwrite('[Output]color_det.png', image_mask)
          
        return image_mask, out

    def grid_det(self, image): 
            
        height = image.shape[0] # y axis
        width = image.shape[1] # x axis
            
        N_H = int(height / self.H_RES)
        N_W = int(width / self.W_RES)
        
        color_map = image[:, :, 2]
        #print(color_map.ndim)
        
        out = np.zeros((N_H, N_W), dtype = int)  
        
        for i in range(0, N_H):
            for j in range(0, N_W):
                #print(i, j)
                sub_arr = color_map[i * self.H_RES : (i + 1) * self.H_RES - 1, \
                                    j * self.W_RES : (j + 1) * self.W_RES - 1]
                sum_col = sub_arr.sum(axis=0)
                sum_all = sum_col.sum()                
                
                
                if sum_all > self.TRD:
                    out[i, j] = 1           
        
        return out
       
'''       
#if __name__ == '__main__':
image_path = 'test.png'
image = cv2.imread(image_path, cv2.IMREAD_UNCHANGED)   
IP_color = Color() # class Color
(mask_image, out) = IP_color.color_det(image)
print(out)  
#out = IP_color.grid_det(image)
'''