import sys
import os
from PIL import Image

#using sys grab 1st and 2n parameter
source = sys.argv[1]
target = sys.argv[2]
#check if folder exists if not create it
if os.path.isdir(target) == False:
    os.mkdir(target)
#loop through entire folder and convert jpg to png
for files in os.listdir(source):
    image = Image.open(f'{source}/{files}')
    new_name = os.path.splitext(files) [0]
    print(new_name)
    image.save(f'{target}/{new_name}.png','png')
    print('Done')
