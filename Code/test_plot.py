# see:
# http://www.loria.fr/~rougier/teaching/matplotlib/#simple-plot
# or:
# http://scipy-lectures.github.com/intro/matplotlib/matplotlib.html
# for more !

import numpy # scientific stuffs
import matplotlib.pyplot as pyplot # to plot


Pi = numpy.pi

x = numpy.linspace(-Pi, Pi, 100)
sin_x = numpy.sin(x)
cos_x = numpy.cos(x)


fig = pyplot.figure()

pyplot.plot(x, sin_x, color="red", linewidth=2.5, linestyle="-",
                       label= 'sin')
pyplot.plot(x, cos_x, color="blue", linewidth=2.5, linestyle="-",
                      label= 'cos')


pyplot.xlim([-Pi * 1.1, Pi * 1.1])
pyplot.ylim([-1.1, 1.1])

#pyplot.xticks([-Pi, -Pi/2, 0, Pi/2, Pi],
#          [r'$-\pi$', r'$-\pi/2$', r'$0$', r'$+\pi/2$', r'$+\pi$'])
pyplot.xticks([-Pi, -Pi/2, 0, Pi/2, Pi],
          ['-Pi', '-Pi/2', '0', 'Pi/2', 'Pi'], color= 'black', fontsize= 10)

pyplot.xlabel('x', fontsize= 13, color= 'black')
pyplot.ylabel('sin(x)', fontsize= 13, color= 'black')

pyplot.legend(loc= 'upper left', frameon= False, title= 'Legend')

pyplot.title('A simple plot.', fontsize= 20)

pyplot.grid(False) # by default


# 1 inch = 2.54 cm
# A4: 21 x 29.7 cm^2

# paper size
w = 29.7    # cm
h = 21.0      # cm

# margins (from the plot zone, *not* including x/y labels !
left = 2   # cm
right = 2  # cm
bottom = 2 # cm
top = 2    # cm

# in % !
left = left / w
right = (w - right) / w
bottom = bottom / h
top = (h - top) / h

# in inches ! :(
w = 29.7 / 2.54
h = 21 / 2.54

fig.set_size_inches(w, h)

# left / right / top / bottom : margins, in % of w/h paper
# wspace, hspace = blank space between subplot, in % of w/h paper
pyplot.subplots_adjust(left= left, bottom= bottom, right= right, top= top,
                    wspace=None, hspace=None)


pyplot.savefig('test.pdf', dpi= 300)
pyplot.show()
