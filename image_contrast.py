# Code by @AmirMotefaker

# Image Manipulation


## Contrast

from PIL import Image, ImageEnhance

#read the image
im = Image.open("image.png")

#image brightness enhancer
enhancer = ImageEnhance.Contrast(im)

factor = 1 #gives original image
im_output = enhancer.enhance(factor)
im_output.save('image_contrast_original.png')

factor = 0.5 #decrease constrast
im_output = enhancer.enhance(factor)
im_output.save('image_contrast_less.png')

factor = 1.5 #increase contrast
im_output = enhancer.enhance(factor)
im_output.save('image_contrast_more.png')

