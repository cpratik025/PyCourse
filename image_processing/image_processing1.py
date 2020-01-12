from PIL import ImageFilter, Image

image = Image.open('shiva.jpg')

print(image.size)
#Compreses the image to tumbnail keeping the aspect ratio
image.thumbnail((400,200))
image.save('thumbnil.jpg')