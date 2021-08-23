import numpy as np
import matplotlib.pyplot as plt


total_ticks = 50
i_c = 30
ticks_from_right = total_ticks - i_c
graph_high = 50


simulated_f_o = np.zeros(total_ticks)


#go rightward
for i in range(total_ticks):
    print(i, end=' ')
    simulated_f_o[i] = i

#go leftward
for i in range(total_ticks-i_c-1):
    print(total_ticks + i, end=' ')
    simulated_f_o[total_ticks-i-1] = (total_ticks + i) - simulated_f_o[total_ticks-i-1]

#graphing separately
ticks = np.array(range(total_ticks))
bars_left = np.array(list(simulated_f_o[:i_c+1]) + [0]*(ticks_from_right-1))
bars_right = np.array([0]*(i_c+1) + list(simulated_f_o[i_c+1:]))

plt.bar(ticks, bars_left)
plt.bar(ticks, bars_right)

plt.vlines(x=i_c+.5, ymin=0, ymax=graph_high, colors='green', label='i_c')

#pointers for lhs and rhs f_o

plt.annotate('lhs f_o', xy=(i_c+.5, i_c/2),
            xytext=(i_c-10, i_c/2),
            xycoords='data', 
            fontsize=10, ha='center', va='center',
            bbox=dict(boxstyle='square', fc='white'),
            arrowprops=dict(arrowstyle='-|>', lw=2.0))

plt.annotate('rhs f_o', xy=(i_c+.5, i_c*3/4-4),
            xytext=(i_c+11, i_c*3/4-4),
            xycoords='data', 
            fontsize=10, ha='center', va='center',
            bbox=dict(boxstyle='square', fc='white'),
            arrowprops=dict(arrowstyle='-|>', lw=2.0))

#Range brackets a, b, c

plt.annotate('a', xy=(10.9, 10),
            xytext=(10.9, 12),
            xycoords='data',                     #draws an arrow from one set of coordinates to the other
            fontsize=8, ha='center', va='center',
            bbox=dict(boxstyle='square', fc='white'),
            arrowprops=dict(arrowstyle='-[, widthB=4.0, lengthB=.5', lw=1.0))   #sets style of arrow and colour)          

plt.annotate('b', xy=(31.9, 27),
            xytext=(31.9, 29),
            xycoords='data',                     #draws an arrow from one set of coordinates to the other
            fontsize=8, ha='center', va='center',
            bbox=dict(boxstyle='square', fc='white'),
            arrowprops=dict(arrowstyle='-[, widthB=4.0, lengthB=.5', lw=1.0))   #sets style of arrow and colour)          

plt.annotate('c', xy=(41.9, 12),
            xytext=(41.9, 14),
            xycoords='data',                     #draws an arrow from one set of coordinates to the other
            fontsize=8, ha='center', va='center',
            bbox=dict(boxstyle='square', fc='white'),
            arrowprops=dict(arrowstyle='-[, widthB=4.0, lengthB=.5', lw=1.0))   #sets style of arrow and colour)          


##Below X axis arrows
plt.annotate('i_c', xy=(.9, .05),
            xytext=(i_c/total_ticks, .05),
            xycoords='figure fraction',                    #draws an arrow from one set of coordinates to the other
            fontsize=10, ha='center', va='center',
            bbox=dict(boxstyle='square', fc='white'),
            arrowprops=dict(arrowstyle='-|>'),   #sets style of arrow and colour
            annotation_clip=False)                               #This enables the arrow to be outside of the plot

plt.annotate('', xy=(i_c/total_ticks-.01, .05),
            xytext=(.15, .05),
            xycoords='figure fraction',                    #draws an arrow from one set of coordinates to the other
            fontsize=8, ha='center', va='center',
            bbox=dict(boxstyle='square', fc='white'),
            arrowprops=dict(arrowstyle='-|>'),   #sets style of arrow and colour
            annotation_clip=False)                               #This enables the arrow to be outside of the plot

plt.annotate('', xy=(.9, .045),
            xytext=(i_c/total_ticks+.01, .045),
            xycoords='figure fraction',                    #draws an arrow from one set of coordinates to the other
            fontsize=8, ha='center', va='center',
            bbox=dict(boxstyle='square', fc='white'),
            arrowprops=dict(arrowstyle='<|-'),   #sets style of arrow and colour
            annotation_clip=False)                               #This enables the arrow to be outside of the plot





plt.title('f_o Toy Demonstration')
plt.legend()
plt.xlim([0,total_ticks])


plt.show()

