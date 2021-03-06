from turtle import *
from math import *
from crstcanvas import CrystalCanvas as crystal

def kernel(x,y, tone):
    freq = 2
    reduce = 0.6
    amp = 0.4
    scatter = 1

    yt = amp*sin(freq*x*3.14)
    diff = 1 - abs(yt-y)/scatter
    impact = diff-reduce

    return tone + impact

c = crystal(kernel=kernel)
c.draw()
mainloop()
