# see:
# http://scipy-lectures.github.com/intro/matplotlib/matplotlib.html
# or (idem):
# http://www.loria.fr/~rougier/teaching/matplotlib/#simple-plot
# for more !
#
# and matplotlib documentation:
# http://matplotlib.org/users/
#
import numpy # scientific stuffs
import matplotlib.pyplot as pyplot # to plot
from matplotlib import rc # LaTeX rendering

import plot_shorthands as plsh # custom useful shothands


# ------ Rendering, see:
# LaTeX: http://matplotlib.org/users/usetex.html
# Mathtext: http://matplotlib.org/users/mathtext.html

# ------ Legend, see:
# http://matplotlib.org/api/pyplot_api.html#matplotlib.pyplot.legend
# http://matplotlib.org/users/legend_guide.html

# ------ Ticks, see:
# http://matplotlib.org/api/pyplot_api.html#matplotlib.pyplot.tick_params


#==============================================================================
# save figure to file
save = True

# display on screen
show = False


#==============================================================================
# Useful shorthands

# ------ Constants
Pi = numpy.pi

# ------ Functions
# See 'plot_shorthands.py' ! 
# ------


#==============================================================================
# ------ 0
# Data to plot
x = numpy.linspace(-Pi, Pi, 100)
sin_x = numpy.sin(x)
cos_x = numpy.cos(x)


# Creating the figure
fig = pyplot.figure()


#==============================================================================
# ------ 1
# Using mathplot rendering
pyplot.subplot(2,2,1)


# ------ Plot commands
pyplot.plot(x, sin_x, color='red', linewidth=2.5, linestyle="-",
                       label= r'$\sin(x)$')
pyplot.plot(x, cos_x, color="blue", linewidth=2.5, linestyle="-",
                      label= 'cos(x)')
# ------


# ------ Axis limits
pyplot.xlim([-Pi * 1.1, Pi * 1.1])
pyplot.ylim([-1.1, 1.1])
# ------


# ------ Ticks
pyplot.xticks([-Pi, -Pi/2, 0, Pi/2, Pi],
              [r'$-\pi$', r'$-\pi/2$', r'$0$', r'$\pi/2$', r'$\pi$'])

pyplot.tick_params(axis= 'x', color= 'cyan', length= 5, width= 2,
                   labelcolor= 'green', labelsize= 13)
pyplot.tick_params(axis= 'y', color= 'violet', length= 10, width= 2,
                   labelcolor= 'grey', labelsize= 13)
# ------


# ------ Axis labels
pyplot.xlabel(r'$x$', fontsize= 13, color= 'black')
pyplot.ylabel('y', fontsize= 13, color= 'black')
# ------


# ------ Legend
leg = pyplot.legend(loc= 'upper left', frameon= False, title= 'Legend')
plsh.set_legend_fontsize(leg, 13) # custom shorthand!
# ------


# ------ Title
pyplot.title('Partial mathtext rendering \n\
LaTeX installation not needed', fontsize= 13, color= 'blue')
# ------


pyplot.grid(False) # by default


#==============================================================================
# ------ 2 - 
# Using LaTeX rendering
rc('text', usetex=1) # LaTeX rendering

pyplot.subplot(2,2,2)


# ------ Plot commands
pyplot.plot(x, sin_x, color="black", linewidth=2.5, linestyle="-.",
                       label= r'$\sin(x)$')
pyplot.plot(x, cos_x, color="green", linewidth=2.5, linestyle="--",
                      label= r'$\cos(x)$')
# ------


# ------ Axis limits
pyplot.xlim([-Pi * 1.1, Pi * 1.1])
pyplot.ylim([-1.1, 1.1])
# ------


# ------ Ticks
pyplot.xticks([-Pi, -Pi/2, 0, Pi/2, Pi],
          [r'$-\pi$', r'$-\pi/2$', r'$0$', r'$\pi/2$', r'$\pi$'])
pyplot.tick_params(axis= 'both', labelsize= 13)
# ------


# ------ Axis labels
pyplot.xlabel(r'$x$', fontsize= 13, color= 'black')
pyplot.ylabel(r'$y$', fontsize= 13, color= 'black')
# ------


# ------ Legend
leg = pyplot.legend(loc= 'upper left')
plsh.set_legend_fontsize(leg, 13) # custom shorthand!
# ------


# ------ Title
title = r'Full \LaTeX\ rendering: '
title+= r'$\displaystyle\sum_{n=1}^\infty\frac{-e^{i\pi}}{2^n}$'

pyplot.title(title, fontsize= 13)
# ------


pyplot.grid(True)


#============================================================================== 
# ------ 3
# Using LaTeX rendering and demonstrating other options
rc('text', usetex=1) # LaTeX rendering
pyplot.subplot(2,2,3)


# ------ Plot commands
pyplot.plot(x, sin_x, color="black", linewidth=2.5, linestyle="-",
                       label= r'$\sin(x)$')
pyplot.plot(x, cos_x, color="cyan", linewidth=2.5, linestyle="-",
                      label= r'$\cos(x)$')
# ------


# ------ Changing the axis
ax = pyplot.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0))
# ------


# ------ Axis limits
pyplot.xlim([-Pi * 1.1, Pi * 1.1])
pyplot.ylim([-1.1, 1.1])
# ------


# ------ Ticks
pyplot.xticks([-Pi, -Pi/2, 0, Pi/2, Pi],
              [r'$-\pi$', r'$-\pi/2$', r'$0$', r'$\pi/2$', r'$\pi$'])
pyplot.tick_params(axis= 'both', labelsize= 13)
# ------


# ------ Legend
leg = pyplot.legend(bbox_to_anchor=(0, 0, 1, 0), mode= 'expand', loc= 2, ncol=2,
              borderaxespad=0., frameon = False)
plsh.set_legend_fontsize(leg, 13) # custom shorthand!
# ------


# ------ Title
title = r'Full \LaTeX\ rendering (again) and other options (1)'
pyplot.title(title, fontsize= 13)
# ------


pyplot.grid(True)


#============================================================================== 
# ------ 4
# Using LaTeX rendering and demonstrating other options

rc('text', usetex=1)  # LaTeX rendering
pyplot.subplot(2,2,4) # subplot

# ------ Plot commands
h_plot_sin_x, = pyplot.plot(x, sin_x, color="red", linewidth=2.5,
                            linestyle="-", label= r'$\sin(x)$')
h_plot_cos_x, = pyplot.plot(x, cos_x, color="blue", linewidth=2.5,
                            linestyle="-", label= r'$\cos(x)$')
# ------

# ------ Changing the axis
ax = pyplot.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0))
# ------

# ------ Setting the axis limits
pyplot.xlim([-Pi * 1.1, Pi * 1.1])
pyplot.ylim([-1.1, 1.1])
# ------


# ------ Settings the ticks
pyplot.xticks([-Pi, -Pi/2, 0, Pi/2, Pi],
              [r'$-\pi$', r'$-\pi/2$', r'$0$', r'$\pi/2$', r'$\pi$'])
pyplot.yticks([-1, -0.5, 0.5, 1],
              [r'$-1$', r'$-0.5$', r'$0.5$', r'$1$'])
pyplot.tick_params(axis= 'both', labelsize= 13)

# Transparency!
for label in ax.get_xticklabels() + ax.get_yticklabels():
    label.set_bbox(dict(facecolor='white', edgecolor='None', alpha=0.85))
# ------


# ------ Annotations
x_ann = 2 * Pi / 3
pyplot.scatter([x_ann, ], [numpy.cos(x_ann), ], 50, color='blue')
pyplot.plot([x_ann, x_ann], [0, numpy.cos(x_ann)], color='blue',
            linewidth=2.5, linestyle="--")

pyplot.annotate(r'$\cos(\frac{2\pi}{3})=-\frac{1}{2}$',
            xy=(x_ann, numpy.cos(x_ann)), xycoords='data',
            xytext=(-90, -50), textcoords='offset points', fontsize=13,
            arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))
# ------


# ------ Legends

# --- cos(x) legend
h_leg_cos_x = pyplot.legend([h_plot_cos_x], [r'$\cos(x)$'], loc=2,
                            frameon= True)
plsh.set_legend_fontsize(h_leg_cos_x, 13) # custom shorthand !

frame  = h_leg_cos_x.get_frame()  
frame.set_facecolor('0.80')    # set the frame face color to light gray

# --- sin(x) legend
h_leg_sin_x = pyplot.legend([h_plot_sin_x], [r'$\sin(x)$'], loc=1,
                            frameon= True, fancybox= True, shadow= True)
plsh.set_legend_fontsize(h_leg_sin_x, 13) # custom shorthand !

# this removes the first legend
# adding it as a separate artist to the axes
pyplot.gca().add_artist(h_leg_cos_x)
# ------


# ------ Title
title = r'Full \LaTeX\ rendering (again) and other options (2)'
pyplot.title(title, fontsize= 13)
# ------


pyplot.grid(False)


#============================================================================== 
if save:
    
    # printing on A4 paper
    width = 29.7    #cm
    height = 21     #cm
    
    #margins
    left = 1.7
    right = 0.5
    
    bottom = 1
    top = 1.5
    
    wspace= 5
    hspace = 4.5
    
    plsh.print_to_file(fig, 'test.pdf', 300, width, height,
                  left, bottom, right, top, wspace, hspace)

if show:    
    pyplot.show()


