import numpy as np
#import cv2

class distance():
    def __init__(self,table):
        self.orientation = table['orientation']     # the orientation that the robot turns
        self.x = table['cor_x'] 
        self.y = table['cor_y'] 
    
    def theta(self):
        return np.arctan(self.x/self.y)
        
    def degree_to_radian(self):
        o_radian = (self.orientation /180 )* np.pi
        return o_radian
    
    def distance_to_landmark(self):
        l_theta = self.theta()  # the degree between landmark and the direction which the robot faces
        a = self.y/np.cos(l_theta)   # the distane to the landmark
        l_a = a * np.sin(self.degree_to_radian() - l_theta)  # the position of landmark for x-axis
        l_b = a * np.cos(self.degree_to_radian() - l_theta)  # the position of landmark for y-axis
        return l_a, l_b # landmark position

if __name__ == '__main__':

    #cor_x = get_table(img_x)  # get the real distance from the table
    #cor_y = get_table(img_y)

    cor_x = 1  # get the real distance from the table
    cor_y = 4

    table = { "orientation": 60,\
			  "cor_x": cor_x ,\
			  "cor_y": cor_y }

    coordination = distance(table)
    land_x, land_y = coordination.distance_to_landmark()
    print(land_x, land_y)