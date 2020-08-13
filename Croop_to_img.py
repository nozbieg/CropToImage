import cv2
import numpy as np
import glob, os

def list_of_files():
    lista=[] 
    for file in glob.glob("*.jpg"):
        lista.append(file)
    return lista 
	
lista = list_of_files()
	
def crop_to_img(img_name) :
    img = cv2.imread(img_name) 
    org_img = cv2.imread(img_name, 1)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
    points = np.argwhere(gray<250) # find where the black pixels are
    points = np.fliplr(points) # store them in x,y coordinates instead of row,col indices
    x, y, w, h = cv2.boundingRect(points) # create a rectangle around those points
    x, y, w, h = x-20, y-20, w+30, h+30 # make the box a little bigger

    cropped_org = org_img[y:y+h, x:x+w]
    cv2.imwrite(img_name, cropped_org)
	
def crop_all(list_of_names) :
    for item in list_of_names :
        crop_to_img(item)
		
if __name__ == "__main__":
    crop_all(lista)
