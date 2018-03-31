from turtle import *
from math import *
from crstcanvas import CrystalCanvas as crystal

def kernel(x,y, tone):
    tone += abs(x)**0.5
    return 1-tone

# c = crystal(res=(300,300), grid_res_y=10, kernel=kernel)
c = crystal(kernel=kernel)
c.draw()
mainloop()
