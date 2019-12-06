# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 17:03:53 2019

@author: mavch
"""
import pygame
import math as m
from ripple import Ripple
from screen import Screen

fps=60
dt = 0.05
size = width, height = 480, 480
res = 60
minColor = 0,0,0
maxColor = 0,0,255

    

if __name__=="__main__":
    pygame.init()    
    pygame.display.set_mode(size)
    
    while True:
        #listen for clicks
            #if click create ripple
        #draw screen