# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from PIL import Image
import numpy as np
import math

w, h = 5000, 6000

data = np.zeros((h, w, 3), dtype=np.int8)

colCnt = 0
for i in range(w):
  value = 125+125.0*math.sin(0.00005*colCnt*i)#*colCnt*1.0)

  for j in range(h):
      data[j,i] = [value, value, value]
  colCnt = colCnt+2
img = Image.fromarray(data, 'RGB')

img.save('my.png')

img.show()
