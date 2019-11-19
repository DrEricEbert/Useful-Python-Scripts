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

colCnt = 0
for i in range(h):
  for j in range(w):
      value = 125+125.0*math.sin(0.1*j)#*colCnt*1.0)
      data[i,j] = [value, value, value]
  colCnt = colCnt+5
img = Image.fromarray(data, 'RGB')

img.save('my.png')

img.show()
