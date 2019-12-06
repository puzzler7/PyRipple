# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 17:42:08 2019

@author: mavch
"""
import pygame
import math as m

class Screen:
    ripples = []
    t = 0
    minCol = (0,0,0)
    maxCol = (0,0,255)
    def __init__(self, minColor, maxColor): 
        self.t = 0
        self.minCol = minColor
        self.maxCol = maxColor
        
    
    def addRipple (self, rip):
        pass
    
    def magToColor(self, mag):
        ret = 0,0,0
        for i in range(3):
            ret[i] = minColor[i]+(maxColor[i]-minColor[i])*mag
        return ret
    
    def draw(self):
        pass
    
    def update(self):
        self.t += dt