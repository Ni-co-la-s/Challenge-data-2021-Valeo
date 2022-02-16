# -*- coding: utf-8 -*-
"""
Created on Thu Jan 20 10:09:05 2022

@author: Nicolas
"""


from PIL import Image, ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True
import re
import glob, os


os.chdir(os.path.dirname(os.path.abspath(__file__)))

X=[]
#______Code servant à voir les différentes dimensions des images__________
os.chdir(os.path.abspath("x_train/1"))
for file in glob.glob("*.jpg"):
    image = Image.open(file)
    width, height = image.size
    if [width,height] not in X:
        X.append([width,height]) 
print(X)




#______Code servant à séparer le dataset en 4, suivant les angles________
os.chdir(os.path.abspath("../.."))
L=["1","2","3","4"]
for path in L:    
    if not os.path.exists(path):
        os.mkdir(path)


regex1 = re.compile("(.*)_(.*)_00_1_._(.*)")
regex2 = re.compile("(.*)_(.*)_00_2_._(.*)")
regex3 = re.compile("(.*)_(.*)_00_3_._(.*)")
regex4 = re.compile("(.*)_(.*)_00_4_._(.*)")
os.chdir(os.path.abspath("x_train/1"))

for file in glob.glob("*.jpg"):
    image = Image.open(file)
    if(bool(re.match(regex1, file))):
        image.save(os.path.abspath("../../1")+"/"+file,'JPEG')
    if(bool(re.match(regex2, file))):
        image.save(os.path.abspath("../../2/")+"/"+file,'JPEG')
    if(bool(re.match(regex3, file))):
        image.save(os.path.abspath("../../3/")+"/"+file,'JPEG')
    if(bool(re.match(regex4, file))):
        image.save(os.path.abspath("../../4/")+"/"+file,'JPEG')


#_______Code servant à redimensionner les images________
os.chdir(os.path.abspath("../../1"))

for file in glob.glob("*.jpg"):
    image = Image.open(file)
    rotated_image1 = image.rotate(-10) 
    width, height=image.size
    ratio_lar=0.15
    ratio_lon=0.45
    left=width/2-width*ratio_lar
    right=width/2+width*ratio_lar
    top=height/2-height*ratio_lon
    bottom=height/2+height*ratio_lon
    cropped_image = rotated_image1.crop((left, top, right, bottom)) 
    os.remove(file, dir_fd=None)

    cropped_image.save(file,'JPEG') 



os.chdir(os.path.abspath("../2"))

for file in glob.glob("*.jpg"):
    image = Image.open(file)
    rotated_image1 = image.rotate(90) 
    width, height=image.size
    ratio_lar=0.15
    ratio_lon=0.45
    left=width/2-width*ratio_lar
    right=width/2+width*ratio_lar
    top=height/2-height*ratio_lon
    bottom=height/2+height*ratio_lon
    cropped_image = rotated_image1.crop((left, top, right, bottom)) 
    os.remove(file, dir_fd=None)

    cropped_image.save(file,'JPEG') 


os.chdir(os.path.abspath("../3"))

for file in glob.glob("*.jpg"):
    image = Image.open(file)
    width, height=image.size
    ratio_lar=0.15
    ratio_lon=0.45
    left=width/2-width*ratio_lar
    right=width/2+width*ratio_lar
    top=height/2-height*ratio_lon
    bottom=height/2+height*ratio_lon
    cropped_image = image.crop((left, top, right, bottom)) 
    os.remove(file, dir_fd=None)

    cropped_image.save(file,'JPEG') 

    
os.chdir(os.path.abspath("../4"))

for file in glob.glob("*.jpg"):
    image = Image.open(file)
    rotated_image1 = image.rotate(100) 
    width, height=image.size
    ratio_lar=0.15
    ratio_lon=0.45
    left=width/2-width*ratio_lar
    right=width/2+width*ratio_lar
    top=height/2-height*ratio_lon
    bottom=height/2+height*ratio_lon
    cropped_image = rotated_image1.crop((left, top, right, bottom)) 
    os.remove(file, dir_fd=None)
    cropped_image.save(file,'JPEG') 



       