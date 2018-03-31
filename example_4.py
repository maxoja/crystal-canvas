from turtle import *
from math import *
from crstcanvas import CrystalCanvas as crystal

def kernel(x,y, tone):
    reduce = 0.6
    slope = 3
    scatter = 1.4

    yt = slope*x
    diff = 1 - (abs(yt-y)/scatter)**1
    impact = diff-reduce
    tone += impact

    return tone

# c = crystal(res=(400,400), grid_res_y=8, kernel=kernel)
c = crystal(kernel=kernel)
c.draw()
mainloop()
