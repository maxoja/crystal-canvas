from turtle import *
from math import *
from crstcanvas import CrystalCanvas as crystal

def kernel(x,y, tone):
    freq = 2
    reduce = 0.6
    amp = 0.4
    scatter = 1

    yt = amp*sin(freq*x*3.14)
    diff = 1 - abs(yt-y)*scatter**-1
    impact = diff-reduce
    tone += impact

    return 1-tone

# c = crystal(res=(600,300), grid_res_y=10, kernel=kernel)
c = crystal(kernel=kernel)
c.draw()
mainloop()
