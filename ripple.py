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
    rings = []
    def __init__(self, x, y, freq = 10, wavelen = .1) :
        self.x = x
        self.y = y
        self.freq = freq
        self.wl = wavelen
        self.v = (m.pi/freq/wavelen)**2
        
    def distFromCenter(self, x, y):
        dx = self.x - x
        dy = self.y - y
        return (dx*dx+dy*dy)**.5
        
    def height (self, x, y, t) :
        dist = self.distFromCenter(x, y)
        if (dist > t*self.v):
            return 0
        return self.A * m.sin(self.wl*(dist-self.freq*t))
        #return self.A * m.sin(self.v*self.distFromCenter(x, y)*t)