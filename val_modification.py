"""modification for the data structure of val dataset"""
import os.path as path
import os
import shutil

# read data from wnids.txt and val_annotations.txt then save to lists
with open('tiny-imagenet-200/wnids.txt') as f:
    dataLines = f.readlines()
    wnids = [item.strip('\n') for item in dataLines]
with open('tiny-imagenet-200/val/val_annotations.txt') as f:
    dataLines = f.readlines()
    val_annotations= []
    for line in dataLines:
        item = line.strip('\n').split('\t')
        val_annotations.append(item)

if not path.exists('tiny-imagenet-200/val_tmp'):
    os.mkdir('tiny-imagenet-200/val_tmp')
for name in wnids:
    # create respective folders for the ids
    os.mkdir(path.join('tiny-imagenet-200', 'val_tmp', name))
for image in val_annotations:
    shutil.copy(path.join('tiny-imagenet-200/val/images/', image[0]),\
                        path.join('tiny-imagenet-200/val_tmp', image[1]))
    # the 0 dimension of image(val_annotations) stands for the image file name,
    # and the 1 dimension of image stands for the respective folder name
os.rename('tiny-imagenet-200/val/', 'tiny-imagenet-200/val_old/')
os.rename('tiny-imagenet-200/val_tmp', 'tiny-imagenet-200/val/')
# change the working val directory to the modified one

print("data structure modification done!")

