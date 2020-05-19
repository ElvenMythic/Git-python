from PIL import Image, ImageFilter
from PIL import ImageEnhance
import time

print("Type your file path")

openIm=input()

img=Image.open(openIm)

size_tuple=img.size
size_list=list(size_tuple)
print("Image resolution -",size_list)

time.sleep(0.5)

print("Your chosen image:")
img.show()

print()

print("Do you want to enhance colors, resize the image, apply a")
print("grayscale filter, rotate the image, or apply a Gaussian blur?")
time.sleep(0.1)
print()
print("Type enhance, resize, grayscale, image, or blur.")
choice=input()
print()





if choice=="enhance":
    img_enh=ImageEnhance.Contrast(img)
    img_enh=img_enh.enhance(1.1)
    img_enh.show()
    print("Save? Y/N")
    choice=input()
    
    if choice=="Y":
        img_enh.save('C:/Users/muffi/Desktop/img_enhanced.png',quality=95)

elif choice=="resize":
    print("What do you want to resize the height by?")
    height=int(input())
    print("What do you want to resize the width by?")
    height=int(input())
    newsize=(size_list[0]*height,size_list[1]*height)
    print(newsize)
    img_resup=img.resize(newsize)
    img_resup.show()
    print("Save? Y/N")
    choice=input()
    
    if choice=="Y":
        img_resup.save('C:/Users/muffi/Desktop/img_resized.png',quality=95)

elif choice=="grayscale":
    img_gscale=img.convert("L")
    img_gscale.show()
    print("Save? Y/N")
    choice=input()
    
    if choice=="Y":
        img_gscale.save('C:/Users/muffi/Desktop/img_grayscale.png',quality=95)

elif choice=="rotate":
    print("Type the amount of degrees you want to rotate your image.")
    rotate=int(input())
    img_rotate=img.rotate(rotate)
    img_rotate.show()
    print("Save? Y/N")
    choice=input()

    if choice=="Y":
        img_gscale.save('C:/Users/muffi/Desktop/img_rotated.png',quality=95)

elif choice=="blur":
    print("Type the amount you want to apply a Guassian blur.")
    blur=int(input())
    img_blur=img.filter(ImageFilter.GaussianBlur(radius=blur)) 
    img_blur.show()
    print("Save? Y/N")
    choice=input()

    if choice=="Y":
        img_blur.save('C:/Users/muffi/Desktop/img_blurred.png',quality=95)
    


