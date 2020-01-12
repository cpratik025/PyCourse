from PIL import Image, ImageFilter
image = Image.open('pikachu.jpg')
#Prints Info of image
print(image)
#prints format of image
print(image.format)
#prints size of the image in dimensions
print(image.size)
#prints mode of the image
print(image.mode)
print(dir(image))

#filter class is called from ImageFilter module and blur is a method inside of it
img_filter = image.filter(ImageFilter.BLUR)
#saving the image as its blured
img_filter.save('blur.png','png')

#filter class is called from ImageFilter module and smooths is a method inside of it
img_filter = image.filter(ImageFilter.SMOOTH)
#saving the image as its smooth
img_filter.save('smooth.png','png')

#convert method of image class is called to change the image to B/W
img_filter = image.convert('L')
#saving the image
img_filter.save('grey.png','png')
#opens up the image
img_filter.show()

img_filter = image
#rotates images to 90 degrees
crocked =img_filter.rotate(90)
crocked.save('grey1.png','png')


img_filter = image
#resizes images to provided dimension
crocked1 =img_filter.resize((300,300))
crocked1.save('grey2.png','png')

img_filter = image
#resizes images to provided dimension
box = (100,100,400,400)
crocked2 =img_filter.crop(box)
crocked2.save('grey3.png','png')



