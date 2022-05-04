from PIL import Image
import os
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

'''
#process image
directory=os.fsencode('blue_ink_frames')
doc=open('blue_ink_datasheet.txt', 'w')
colour=0
total=0

index=0
while index<=392:
    filename=f'blue_ink_frames/frame{index}.jpg'
    image=Image.open(filename, 'r')
    pix=image.load()
    width, height=image.size    
    colour=0
    for i in range(width):
        for j in range(height):
            if pix[i,j][0]<30 and pix[i,j][1]<30 and pix[i,j][2]>50:
               colour+=1
    total=width*height
    doc.write(str(colour/total)+'\n')
    print(filename," successfully processed")
    image.close()
    index+=1
doc.close()
'''
#graph
doc=open('blue_ink_datasheet.txt', 'r')
red=doc.read()

y=red.split('\n')
y = [float(x) for x in y if x!='']
time=0.0
x=[]
for i in range(len(y)):
    x.append(time)
    time+=1/240

#f=lambda x,a,b,c: a*np.log(b*x+c)

#popt, pcov = curve_fit(f, x, y, p0=(1,1,1))
#print(popt)

#foundf=lambda x: popt[0]*np.log(popt[1]*x+popt[2])
#foundy=[foundf(k) for k in x]

plt.plot(x,y,marker='.', label='experimental data')
#plt.plot(x,foundy,label=f'{popt[0]}ln({popt[1]}x+{popt[2]})')
plt.title("The Growth of Area Ratio of Blue Ink")
plt.xlabel("time [s]")
plt.ylabel("Area ratio [no unit]")
plt.legend()
plt.grid()
plt.show()


'''

#checking fitness of ln model
def linearity(x,a,b):
    return a*x+b
poptnew, pcov = curve_fit(linearity, foundy, y, p0=(1,1))
print(poptnew)
linearityy=[linearity(z, poptnew[0], poptnew[1]) for z in foundy]
plt.plot(foundy, y)
plt.plot(foundy, linearityy, label=f'{poptnew[0]}x+{poptnew[1]}')
plt.xlabel(f'{popt[0]}ln({popt[1]}x+{popt[2]})')
plt.ylabel('Area Ratio')
plt.title(f'A={popt[0]}ln({popt[1]}x+{popt[2]})')
plt.grid()
plt.legend()
plt.show()
'''