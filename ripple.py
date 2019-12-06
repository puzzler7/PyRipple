# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 17:42:51 2019

@author: mavch
"""
import pygame
import math as m

class Ripple:
    x = 0
    y = 0
    A = 1
    v = 1
    rings = []
    def __init__(self, x, y) :
        self.x = x
        self.y = y
        
    def distFromCenter(self, x, y):
        dx = self.x - x
        dy = self.y - y
        return (dx*dx+dy*dy)**.5
        
    def height (self, x, y, t) :
        #return self.A * m.sin(.05*x+t)
        return self.A * m.sin(0.1*(self.distFromCenter(x, y)-5*t))
        #return self.A * m.sin(self.v*self.distFromCenter(x, y)*t)