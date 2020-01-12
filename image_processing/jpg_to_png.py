import sys
import os
from PIL import Image

#using sys grab 1st and 2n parameter
source = sys.argv[1]
target = sys.argv[2]
#check if folder exists if not create it
if os.path.isdir('new') == False:
    os.mkdir('new')
#loop through entire folder and convert jpg to png
for files in os.listdir(sys.argv[1]):
    image = Image.open(f'{source}')
    image.save(f'{target}{files}.png','png')
