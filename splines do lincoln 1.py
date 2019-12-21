from __future__ import print_function
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import scipy.interpolate
from PIL import Image
from pylab import *


x = [1,6,7,10,12]
y = [7,9,60,90,201]
xvals = np.linspace(0, 8, 150)
func = scipy.interpolate.splrep(x, y, s=0, k=3)
yvals = scipy.interpolate.splev(xvals, func, der=0)

plt.figure()
plt.plot(x, y, 's', xvals, yvals,'k', x, y, 'r')
plt.legend(['Pontos', 'Spline cúbico', ' Linear'])
plt.axis([0, 8,0, 600])
plt.title('interpolação spline cúbica')
plt.show()
