import random
from itertools import count
from tkinter import X
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import gc
gc.enable()
plt.style.use('fivethirtyeight')

x_vals=[]
y_vals=[]

index=count()

def animate(i):
    x_vals.append(next(index))
    y_vals.append(random.randint(0,5))
    plt.plot(x_vals, y_vals)

ani=FuncAnimation(plt.gcf(), animate) #interval in milliseconds, gcf=get current function

plt.tight_layout()
plt.show()