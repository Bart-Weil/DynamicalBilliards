import math
import numpy as np
from PIL import Image, ImageDraw

w = 500
l = 500

imgx = w
imgy = l
image = Image.new("RGB", (imgx, imgy))
draw = ImageDraw.Draw(image)

class Bunimovich:

    #l and w are the width and length of the bounding rectangle

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def flatbordersolve(self, bilxp, bilyp, bilx, bily, state):

        if state == 0:

            d = 1
            e = 0
            f = self.width

        else:

            d = 1
            e = 0
            f = 0

        a = bilxp - bilx
        b = bilyp - bily
        c = a * (bilxp) + b * (bilyp)

        A = np.array([a, b], [c, d])
        B = np.matmul(np.linalg.inv(A), np.array([c, f]))

        return [B[0], B[1]]

    def rcheck(self, bilx, bily):

        check = 0

        if math.sqrt(bilx**2+bily**2)<self.width/2:

            check = 1

        if math.sqrt((bilx-self.length)**2 + (bily-w/2)**2)<self.width/2:

            check = 1

        return check

    def check(self, bilx, bily):

        check = 0

        if 0<bilx<self.length and 0<bily<self.width:

            pass

        if self.rcheck(bilx, bi ly) == 0:

            pass

        else:

            check = 1


    def reflectflat(self, bilxp, bilyp, bilx, bily):

        if
