from turtle import *
from math import *
from crstcanvas import CrystalCanvas as crystal

def kernel(x,y, tone):
    reduce = 0.6
    slope = 3
    scatter = 1.4

    yt = slope*x
    diff = 1 - abs(yt-y)/scatter
    impact = diff - reduce

    return tone + impact

c = crystal(kernel=kernel)
c.draw()
mainloop()
