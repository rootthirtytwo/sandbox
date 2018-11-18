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

#fig4.savefig('test.png', dpi=200)# to save the image in a file


'''
loc : int or string or pair of floats, default: 'upper right'
    The location of the legend. Possible codes are:

        ===============   =============
        Location String   Location Code
        ===============   =============
        'best'            0
        'upper right'     1
        'upper left'      2
        'lower left'      3
        'lower right'     4
        'right'           5
        'center left'     6
        'center right'    7
        'lower center'    8
        'upper center'    9
        'center'          10
        ===============   =============


    Alternatively can be a 2-tuple giving ``x, y`` of the lower-left
    corner of the legend in axes coordinates (in which case
    ``bbox_to_anchor`` will be ignored).
'''

fig5 = plt.figure()
axes5 = fig5.add_axes([0,0,1,1])
axes5.plot(x,x**2, label = "x square")
axes5.plot(x,x**3, label = "x cube")
axes5.legend(loc=0)

#more plot properties
fig5 = plt.figure()
axes5 = fig5.add_axes([0,0,1,1])
axes5.plot(x,x**2, label = "x square", color="#A458A6", linewidth=5, alpha = 0.8 \
           ,linestyle='-', marker='*', markersize=20, markerfacecolor='red' \
           , markeredgewidth=1, markeredgecolor='blue')
axes5.legend(loc=0)
