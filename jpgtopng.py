import sys
import os
from PIL import Image

#grabbing args from User input
input_folder=sys.argv[1]
output_folder=sys.argv[2]

if not os.path.exists(output_folder):
  os.makedirs(output_folder)

for filename in os.listdir(input_folder):
  img=Image.open(f'{input_folder}{filename}')
  name=os.path.splitext(filename)[0]
  img.save(f'{output_folder}{name}.png','png')