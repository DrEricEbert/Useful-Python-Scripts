# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from PIL import Image
import numpy as np
import math

w, h = 500, 600

data = np.zeros((h, w, 3), dtype=np.int8)
for j in range(h):
    for i in range(w):
        value = 125+125.0*math.sin(.1*i)#*colCnt*1.0)
        data[j,i] = [value, value, value]
img = Image.fromarray(data, 'RGB')
img.save('my.png')
img.show()
