from __future__ import print_function
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import scipy.interpolate
from PIL import Image
from pylab import *


x = [2,4,5,8,9,10]
y = [0.1559,0.17,0.21,0.2444,0.323,0.5]

xvals = np.linspace(0, 7.5, 150)
func = scipy.interpolate.splrep(x, y, s=0, k=3)
yvals = scipy.interpolate.splev(xvals, func, der=0)

plt.figure()
plt.plot(x, y, 's', xvals, yvals,'k', x, y, 'r')
plt.legend(['Pontos', 'Spline cúbico', ' Linear'])
plt.axis([1, 7.5 ,0, .9])
plt.title('Interpolação Cúbica')
plt.show()
