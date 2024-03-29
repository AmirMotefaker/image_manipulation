# Code by @AmirMotefaker

# Image Manipulation


## Sharpening

from PIL import Image, ImageDraw

# Load image:
input_image = Image.open("image.png")
input_pixels = input_image.load()

# High-pass kernel
kernel = [[  0  , -.5 ,    0 ],
          [-.5 ,   3  , -.5 ],
          [  0  , -.5 ,    0 ]]

# Middle of the kernel
offset = len(kernel) // 2

# Create output image
output_image = Image.new("RGB", input_image.size)
draw = ImageDraw.Draw(output_image)

# Compute convolution with kernel
for x in range(offset, input_image.width - offset):
    for y in range(offset, input_image.height - offset):
        acc = [0, 0, 0]
        for a in range(len(kernel)):
            for b in range(len(kernel)):
                xn = x + a - offset
                yn = y + b - offset
                pixel = input_pixels[xn, yn]
                acc[0] += pixel[0] * kernel[a][b]
                acc[1] += pixel[1] * kernel[a][b]
                acc[2] += pixel[2] * kernel[a][b]

        draw.point((x, y), (int(acc[0]), int(acc[1]), int(acc[2])))
    
output_image.save("image_sharpening_output.png")
