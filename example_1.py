from turtle import *
from math import *
from crstcanvas import CrystalCanvas as crystal

def kernel(x,y, tone):
    divisor = (abs(x) + abs(y))*8
    return tone/divisor

c = crystal(kernel=kernel)
c.draw()
mainloop()