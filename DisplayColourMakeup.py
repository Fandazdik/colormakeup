from PIL import Image, ImageStat
import math
import colorsys
import imageio
import os
import time
import datetime

SINKFILE = '/home/pi/Desktop/PYTHON/Util/gifsplit/colourprofile.png'
SOURCEFILE = '/home/pi/Downloads/sortedstuff/tragia-lucario.jpeg'
TEMPFILE = '/home/pi/Desktop/PYTHON/Util/gifsplit/resulttest.png'


def get_hsv(im_link):
    im2 = Image.open(im_link,'r')
    hsv_pix = list(im2.getdata())
    hsv_list = []
    for tup in hsv_pix:
        new_tup = colorsys.rgb_to_hsv(tup[0], tup[1], tup[2])
        hsv_list.append((math.degrees(new_tup[0]), math.degrees(new_tup[1]), new_tup[2]))
    return hsv_list

itr = lambda itera : str((100+int(itera)))[1:]


size = os.stat(SOURCEFILE).st_size

itera = 0
highestH = 0
mid_val = 0

im = Image.open(SOURCEFILE, 'r')
im.save(TEMPFILE)

width = im.size[0]
height = im.size[1]

im = im.convert('RGB')

pix_val = list(im.getdata())

newimg = Image.new('RGB', (width, height), color = (0,0,0))


pixel_map = newimg.load()

len_num = width*height
pixels_out = []
images = []

hs_square = Image.open('hs_square.png','r')

hsv_pixels = get_hsv(TEMPFILE)

hsv_map = hs_square.load()

for tup in hsv_pixels:
    x = int(tup[0]*6)
    y = int(tup[1]*6)
    
    
    (r, g, b) = colorsys.hsv_to_rgb(math.radians(tup[0]), math.radians(tup[1]), tup[2])
    
    hsv_map[(x, y)] = (int(r), int(g), int(b))
 
hs_square.show()
hs_square.save(SINKFILE)

