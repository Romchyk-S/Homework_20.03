# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 16:27:29 2024

@author: romas
"""

import numpy as np

def func_0():
    
    x = np.arange(-10, 10, 0.1)
    
    label = "$x^2-4x+3$"
    
    title = "$y > 0: x \in (-\infty;1) \cup (3;+\infty) \ \ y < 0: x \in (1;3)$"
    
    return x, x**2-4*x+3, label, title

def func_1():
    
    x = np.arange(-10, 10, 0.1)
    
    label = "$x^2-6x+9$"
    
    title = "$y > 0: x \in (-\infty;3) \cup (3;+\infty)$"
    
    return x, x**2-6*x+9, label, title

def func_2():
    
    x = np.arange(-10, 10, 0.1)
    
    label = "$x-x^2$"
    
    title = "$y > 0: x \in (0;1) \ \ y < 0: x \in (-\infty;0) \cup (1;+\infty)$"
    
    return x, x-x**2, label, title

def func_3():
    
    x = np.arange(-10, 10, 0.1)
    
    label = "$x-1-x^2$"
    
    title = "$y < 0: x \in \Re $"
    
    return x, x-1-x**2, label, title

def func_4():
    
    x = np.arange(1.01, 10, 0.1)
    
    label = "$log_{1/2} (x-1)$"
    
    title = "$y > 0: x \in (1;2) \ \ y < 0: x \in (2;+\infty)$"
    
    return x, np.emath.logn(1/2, x-1), label, title

def func_5():
    
    label = "$log_{1/2} (-x)$"
    
    title = "$y > 0: x \in (-1;0) \ \ y < 0: x \in (-\infty;-1)$"
    
    x = np.arange(-10, -0.01, 0.1)
    
    return x, np.emath.logn(1/2, -x), label, title

def func_6():
    
    x = np.arange(-10, 10, 0.1)
    
    y = (np.piecewise(x, [(x < 0.99), ((x >= 0.99) & (x <= 1.01)), (x>1.01)],
                          [lambda x: 12/(x-1), np.nan, lambda x: 12/(x-1)]))
    
    label = "$12/(x-1)$"
    
    title = "$y > 0: x \in (1;+\infty)  \ \ y < 0: x \in (-\infty;1)$"

    return x, y, label, title

def func_7():
    
    x = np.arange(-10, 10, 0.1)
    
    y = (np.piecewise(x, [(x < 1.99), ((x >= 1.99) & (x <= 2.01)), (x>2.01)],
                          [lambda x: (3*x+5)/(x-2), np.nan, lambda x: (3*x+5)/(x-2)]))
    
    label = "$(3x+5)/(x-2)$"
    
    title = "$y > 0: x \in (-\infty;5/3) \cup (2;+\infty) \ \ y < 0: x \in (5/3;2)$"
  
    return x, y, label, title

def func_8():
 
    x = np.arange(-10, 10, 0.1)
    
    y = (np.piecewise(x, [(x < 0.99), ((x >= 0.99) & (x <= 1.01)), ((x > 1.01) & (x < 2.99)),
                          ((x >= 2.99) & (x <= 3.01)), (x > 3.01)],
                          [lambda x: (x-2)/(x**2-4*x+3), np.nan, lambda x: (x-2)/(x**2-4*x+3), np.nan, lambda x: (x-2)/(x**2-4*x+3)]))
    
    label = "$(x-2)/(x^2-4x+3)$"
    
    title = "$y > 0: x \in (1;2) \cup (3;+\infty) \ \ y < 0: x \in (-\infty;1) \cup (2;3)$"
  
    return x, y, label, title

def func_9():
    
    x = np.arange(-10, 10, 0.1)
    
    y = (np.piecewise(x, [(x < -1.01), ((x >= -1.01) & (x <= -0.99)), ((x > -0.99) & (x < 6.99)),
                          ((x >= 6.99) & (x <= 7.01)), (x > 7.01)],
                          [lambda x: (x**2-5*x+6)/(x**2-5*x-6), np.nan, lambda x: (x**2-5*x+6)/(x**2-5*x-6), np.nan, lambda x: (x**2-5*x+6)/(x**2-5*x-6)]))
    
    y[:-1][np.abs(np.diff(y)) > 50] = np.nan
    
    label = "$(x^2-5x+6)/(x^2-5x-6)$"
    
    title = "$y > 0: x \in (-\infty;-1) \cup (2;3) \cup (6;+\infty) \ \ y < 0: x \in (-1;2) \cup (3;6)$"
  
    return x, y, label, title

def func_9_1():
    
    x = np.arange(-10, 10, 0.1)
    
    label = "$sin(2x)$"
    
    title = "$y > 0: x \in (0+\pi_n; \pi/2+\pi_n) \ \ y < 0: x \in (\pi/2 +\pi_n;\pi+\pi_n) \ \ n = 0,1,2... $"
  
    return x, np.sin(2*x), label, title


def func_9_2():
    
    x = np.arange(-0.5, 0.5, 0.01)
    
    label = "$arccos(2x)$"
    
    title = "$y > 0: x \in (-1/2;1/2)$"
  
    return x, np.arccos(2*x), label, title
