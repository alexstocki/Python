# Conversor de images. Levanta todas los archivos con extension .JPG 
# y guarda las imagenes convertidas en .PNG dentro del directorio que
# se pasa como segundo parametro

import sys, os, glob
from PIL import Image

def get_clean_name(raw_name):
    raw_name = raw_name.split('/')
    clean_name = str(raw_name[1])
    return clean_name.replace('.jpg', '')

dir_base, dir_new = sys.argv[1], sys.argv[2]

if not os.path.exists(str(dir_new)):
    os.makedirs(dir_new)

images_list = []

for images in glob.iglob(f'{dir_base}*.jpg'):
    images_list.append(images)

for img in images_list:
    image = Image.open(img)
    clean_name_img = get_clean_name(img)
    image.save(f'{dir_new}{clean_name_img}.png', 'png')

print('Proceso terminado\n')