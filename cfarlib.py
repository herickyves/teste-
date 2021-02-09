#--------------------------------------------------------------------#
# Developed by BRAIN - Brazilian Artificial Inteligence Nucleus      #
# Unversity FACENS, Sorocaba, Brazil, 2021.                          #
# Developers: Herick Y. S. Ribeiro, Luiz H. Aguiar.                  #
# e-mails: herick.ribeiro@facens.br, luizh5391@gmail.com             #
#--------------------------------------------------------------------#


#--------------------------------------------------------------------#
#--------------------------- Libraries ------------------------------#
#--------------------------------------------------------------------#

import numpy as np
import h5py
import matplotlib.pyplot as plt
import cv2
import numpy.matlib

#--------------------------------------------------------------------#
#--------------------------- Classes --------------------------------#
#--------------------------------------------------------------------#

class cfarlib():

    def __init__(self):
        pass

    # This method convert radar's data already processed (by FFTs) into images to use in OpenCV functions.
    # In this method only 2D data are accepted.
    def cvtData2img(self,heatmaps, width, height):
    
        data = np.expand_dims(np.array(list(heatmaps)),axis=2)              # Expand a axis to create a image
        blank_image = np.zeros((width,height,3), np.uint8)                  # Create a empty image 
        data = blank_image+data                                             # Add the data to a empty image
        image = cv2.cvtColor(data.astype('uint8'),cv2.COLOR_BGR2GRAY)       # Convert data in openCV images
        return image
    
    def CFAR(self, data, type):
        pass
    
    def CFAR2D(self, data, type):
        pass

    def CFARCV(self, dataCV, typeCV, blockSize, c, limit = 120):

        dataCV = np.array(dataCV)
        shapeData = np.array(dataCV).shape
        width = shapeData[0]
        height = shapeData[1]
        dataResult = self.cvtData2img(dataCV, width, height) 

        if(typeCV == 'mean'):
            img_thr = cv2.adaptiveThreshold(dataResult,limit,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,blockSize,c)    
        elif(typeCV == 'gaussian'):
            img_thr = cv2.adaptiveThreshold(dataResult,limit,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,blockSize,c)
        else:    
            raise TypeError("Invalid Type, try 'mean' or 'gaussian'")
        dataResult[np.where(img_thr == 0)] = 0
        
        return dataResult