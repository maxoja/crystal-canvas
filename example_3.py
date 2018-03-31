from turtle import *
from math import *
from crstcanvas import CrystalCanvas as crystal

def kernel(x,y, tone):
    addition = sqrt(abs(x))
    return 1 - (tone + addition)

c = crystal(kernel=kernel)
c.draw()
mainloop()
