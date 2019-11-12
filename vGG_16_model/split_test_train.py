import os
import shutil
from imutils import paths
from pyimagesearch import config

FROM_URL = 'images/'
TO_URL = 'input/'

# filter into 11 artists with >200 images 
# filtered = ['Vincent_van_Gogh', 'Edgar_Degas', 'Pablo_Picasso', 'Pierre-Auguste_Renoir', 'Albrecht_Dürer', 'Paul_Gauguin',
#             'Francisco_Goya', 'Rembrandt', 'Alfred_Sisley', 'Titian', 'Marc_Chagall']

filtered = config.CLASSES

# Convert images into split folder input 
p = os.path.sep.join([FROM_URL])
imagePaths = list(paths.list_images(p))

# Create a new dir for each class label
root = os.getcwd() + "/"
to_path = root + TO_URL
print(root)

for i in imagePaths:
    label = "_".join(i.split(os.path.sep)[-1].split('_')[0:-1])
    if label not in filtered: 
        print("skip " + label)
        continue
    dirName = to_path + label
    if not os.path.exists(dirName):
        os.mkdir(dirName)
        print("Created Directory: " , dirName)
    
    # copy image into new dir
    rootImage = root + i
    newPath = dirName + "/" + i.split(os.path.sep)[-1]
    shutil.copyfile(rootImage, newPath)