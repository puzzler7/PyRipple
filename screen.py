# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 17:42:08 2019

@author: mavch
"""
import pygame
import math as m
from ripple import Ripple

class Screen:
    ripples = []
    t = 0
    minCol = (0,0,0)
    maxCol = (0,0,255)
    res = 60
    dt = 0.05
    pyScreen = None
    def __init__(self, size, res, dt, minColor, maxColor): 
        self.t = 0
        self.size = size
        self.res = res
        self.dt = dt
        self.minCol = minColor
        self.maxCol = maxColor
        self.pixelSize = size[0]/res, size[1]/res
            
    def addRipple (self, rip):
        self.ripples.append(rip)
    
    
    
    def draw(self):
        pass
    
    def update(self):
        self.t += self.dt