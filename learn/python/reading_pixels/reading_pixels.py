from PIL import Image
from itertools import count
import matplotlib.pyplot as plt

image = Image.open("reading_pixels_iamge.jpg", 'r')
pix=image.load()
print(pix[0,0])
print(pix[600,450])