#libraries
import matplotlib.pyplot as plt
import numpy as np

# variables
x = np.linspace(0,5,11)
y = x ** 2

# working with objects
#single chart
fig = plt.figure()
axes = fig.add_axes([0.1,0.1,0.8,0.8]) # [left, bottom, width,height]
axes.plot(x,y)
axes.set_xlabel('x')
axes.set_ylabel('y')
axes.set_title('Simple Chart')

#multi chart
fig1 = plt.figure()
axes1 = fig1.add_axes([0.1,0.1,0.8,0.8])
axes2 = fig1.add_axes([1,0.1,0.8,0.8])

axes1.plot(x,y)
axes1.set_xlabel('x')
axes1.set_ylabel('y')
axes1.set_title('Chart One')

axes2.plot(x,y)
axes2.set_xlabel('x')
axes2.set_ylabel('y')
axes2.set_title('Chart Two')


#subplot
fig3, axes3 = plt.subplots(nrows=1,ncols=2)

for a in axes3:
    a.plot(x,y)

fig3.tight_layout()


# more advance
fig4 = plt.figure(figsize=(3,2))# width, height
axes4 = fig4.add_axes([0,0,1,1])
axes4.plot(x,y)

fig4.savefig('test.png', dpi=200)