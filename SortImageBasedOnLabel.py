''' This program will copy images from scr_dir to dst_dir_1 and dst_dir_2 based on the label provided in the csv file.
if label is 0 ,image is copied to dst_dir_1 and 
if label is 1 ,image is copied to dst_dir_2 .'''

# Import the required libraries
import os
import glob
import shutil
import pandas as pd

dirname = "train80" 
# dirname is the name of the directory whose images are to be copied to different folder based on label

# To rename images in dirname folder
#for i, filename in enumerate(os.listdir(dirname)):
    #print(filename)
    #os.rename(dirname + "/" + filename, dirname + "/" + "c"+str(i) + ".png")


# Printing the file names which is in dirname
for i, filename in enumerate(os.listdir(dirname)):
    print(filename)


# Reading the csv file
df = pd.read_csv('Label80withHeader.csv')
df.head()


# creating folders to copy images to it based on label
os.mkdir("Label0")
os.mkdir("Label1")


# Printing ImageId and label of the csv file
for index, row in df.iterrows():
    print(row['ImageId'], row['label'])


#Copying logic.
# src_dir is the path of source directory which contains the images to be sorted
src_dir = "/home/sinchu-sr/Mini-Project/histopathologic-cancer-detection/SplitData/train80"
# dst_dir_1 is the path of directory where images are copied if the label is 0
dst_dir_1 = "/home/sinchu-sr/Mini-Project/histopathologic-cancer-detection/SplitData/Label0"
# dst_dir_2 is the path of directory where images are copied if the label is 1
dst_dir_2 = "/home/sinchu-sr/Mini-Project/histopathologic-cancer-detection/SplitData/Label1"

for index, row in df.iterrows():
    print(row['ImageId'], row['label'])
    ImageId = row['ImageId']
    Label = row['label']
    img_name = ImageId+".jpeg"
    if(Label == 0):
        shutil.copy(src_dir+"/"+img_name,dst_dir_1)
    else:
        shutil.copy(src_dir+"/"+img_name,dst_dir_2)

