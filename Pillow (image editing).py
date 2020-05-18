from PIL import Image, ImageFilter
from PIL import ImageEnhance
import time



lakeside=Image.open('C:/Users/muffi/Pictures/Lakeside-873 (Cropped).png')

size_tuple=lakeside.size
size_list=list(size_tuple)
print(size_list)

newsize=(size_list[0]*2,size_list[1]*2)

print(newsize)

lakeside.show()
time.sleep(3)
lakeside_enh=ImageEnhance.Contrast(lakeside)
lakeside_enh.enhance(1.1).show()
time.sleep(3)
lakeside_resup=lakeside.resize(newsize)
lakeside_resup.show()
