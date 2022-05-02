from PIL import Image
from itertools import count
import matplotlib.pyplot as plt

image = Image.open("reading_pixels_image.jpg", 'r')
pix=image.load()
width, height = image.size

for i in range(width):
    for j in range(height):
        print(f'{pix[i,j]}\t{i} {j}')