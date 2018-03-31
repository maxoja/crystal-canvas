from turtle import *
from math import *
from crstcanvas import CrystalCanvas as crystal


def kernel(x,y, tone):
    tone /= (abs(x) + abs(y))*8
    return tone


# c = crystal(res=(300, 300), grid_res_y=10, kernel=kernel)
c = crystal(kernel=kernel)
c.draw()
mainloop()