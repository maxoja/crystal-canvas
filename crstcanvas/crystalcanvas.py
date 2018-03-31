from turtle import *
from math import *
from random import *

class CrystalCanvas:
    def __init__(self, res=(300,300), grid_res_y=3, margin=50, kernel=lambda a,b,t: t):
        res_x, res_y = res
        self.scale = res_y/grid_res_y/4
        self.grid_res = {
            'y':grid_res_y,
            'x':ceil(res_x/self.scale/4)
        }

        size_x = res_x + margin
        size_y = res_y + margin

        setup(size_x, size_y)
        tracer(False)
        ht()

        print('grid resolution :', (self.grid_res['x'], self.grid_res['y']))
        print('image resolution :', res)
        print('canvas resolution :', (size_x, size_y))

        self.kernel = kernel

    def triangle(self, align, xg, yg):
        goto(xg*self.scale, yg*self.scale)

        adjusted_x = xg + ( 0.5 if align <= 1 or align >= 6 else -0.5 )
        adjusted_x /= 2*(self.grid_res['x']+0.25)
        adjusted_y = yg + ( 0.5 if align < 4 else -0.5 )
        adjusted_y /= 2*(self.grid_res['y']+0.25)
##        print(adjusted_x, adjusted_y)
        
        tone = random()
        tone = self.kernel(adjusted_x, adjusted_y, tone)
        tone = 1 if tone > 1 else 0 if tone < 0 else tone
        fillcolor((tone,)*3 )

        begin_fill()
        
        if align%2 == 0:
            seth(align*45)
            fd(self.scale)
            lt(90)
            fd(self.scale)
            lt(135)
            fd(sqrt(2)*self.scale)
            
        else:
            seth(align*45)
            fd(sqrt(2)*self.scale)
            lt(135)
            fd(self.scale)
            lt(90)
            fd(self.scale)

        end_fill()

    def draw(self):
        clear()
        pu()
        for i in range(-self.grid_res['x'],self.grid_res['x']+1):
            for j in range(-self.grid_res['y'],self.grid_res['y']+1):
                for k in range(8):
                    self.triangle(k, i*2, j*2)

