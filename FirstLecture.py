# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 19:18:13 2020

@author: Edward
"""

import numpy as np
import matplotlib.pyplot as mpl

start = 0
stop = 10 * np.pi
step = 0.1

x = np.arange(start, stop, step)
y = np.sin(x)

r = np.cos(x*8)

mpl.plot(x,y)
mpl.plot(x,r)
mpl.show()