#libraries
import matplotlib.pyplot as plt
import numpy as np

# variables
x = np.linspace(0,5,11)
y = x ** 2

plt.subplot(1,2,1) # rows, columns, plot number
plt.plot(x,y,'r')
plt.subplot(1,2,2)
plt.plot(y,x,'b')
plt.show()