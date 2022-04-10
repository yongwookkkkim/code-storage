import math
import random
import numpy as np
import matplotlib.pyplot as plt

def approxPi(repetition):
    inCircle=0
    for i in range(repetition):
        x=random.random()*100.0
        y=random.random()*100.0
        if (x-50)**2 + (y-50)**2 <= 2500:
            inCircle+=1.0
    return inCircle/repetition*4.0

print(approxPi(5000000))