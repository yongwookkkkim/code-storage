from calendar import c
from PIL import Image
import os
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from scipy.stats import chisquare
from scipy import stats

doc=open('black_ink_datasheet.txt', 'r')
red=doc.read()

y=red.split('\n')
y = [float(x) for x in y if x!='']
time=0.0
x=[]
for i in range(len(y)):
    x.append(time)
    time+=1/6

lnx=[np.sqrt(z) for z in x]
res=stats.linregress(lnx,y)
def f(x):
    return res.slope*np.sqrt(x)+res.intercept
foundy=[f(k) for k in x]
result=chisquare(y, f_exp=foundy)
print(result)

#f=lambda x,a,b,c: a*np.log(b*x+c)

#popt, pcov = curve_fit(f, x, y, p0=(1,1,1))
#print(popt)

#foundf=lambda x: popt[0]*np.log(popt[1]*x+popt[2])
#foundy=[foundf(k) for k in x]

#res=chisquare(y, f_exp=foundy)
#print(res)

plt.plot(x, foundy, label=f'{res.slope}sqrt(x)+{res.intercept}')
plt.plot(x,y,marker='.', label='experimental data')
plt.title("The Growth of Area Ratio of Black Ink")
plt.xlabel("time [s]")
plt.ylabel("Area ratio [no unit]")
plt.legend()
plt.grid()
plt.show()


'''
directory=os.fsencode('black_ink_frames')
doc=open('black_ink_datasheet.txt', 'w')
colour=0
total=0


index=0
while index<=7710:
    filename=f'black_ink_frames/frame{index}.jpg'
    image=Image.open(filename, 'r')
    pix=image.load()
    width, height=image.size    
    colour=0
    for i in range(width):
        for j in range(height):
            if pix[i,j][0]<90 and pix[i,j][1]<90 and pix[i,j][2]<90:
               colour+=1
    total=width*height
    doc.write(str(colour/total)+'\n')
    print(filename," successfully processed")
    image.close()
    index+=30
'''