# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 17:03:53 2019

@author: mavch
"""
import pygame
import math as m
import sys
from ripple import Ripple

fps=60
t = 0
dt = 1
size = width, height = 500, 500
res = 100
pixelSize = size[0]/res, size[1]/res
minColor = 0,0,0
maxColor = 0,255,0
ripples = []

def magToColor(mag):
    ret = [0,0,0]
    mag = mag/2+.5
    for i in range(3):
        ret[i] = minColor[i]+(maxColor[i]-minColor[i])*mag
    return ret

def draw():
    for i in range(res):
        for j in range(res):
            height = 0
            for rip in ripples:
                height += rip.height(i*pixelSize[0], j*pixelSize[1], t)
            height = max(min(height,1), -1)
            color = magToColor(height)
            #for i in range(3):
                #color[i] = min(max(color[i],0),255)
            rect = pygame.Rect(i*pixelSize[0], j*pixelSize[1], pixelSize[0], pixelSize[1])
            pygame.draw.rect(screen, color, rect)

    

if __name__=="__main__":
    pygame.init()    
    screen = pygame.display.set_mode(size)
    t = 0
    screen.fill(magToColor(0))
    rip = Ripple(size[0]//4,size[1]//2)
    rip1 = Ripple(3*size[0]//4,size[1]//2)
    rip2 = Ripple(size[0]//2,size[1]//4)
    rip3 = Ripple(size[0]//2,3*size[1]//4)
    ripples.append(rip)
    ripples.append(rip1)
    ripples.append(rip2)
    ripples.append(rip3)
    
    while True:
        draw()
        #screen.fill((0,0,255))
        t += dt
        for event in pygame.event.get():  #praxis stuff
            if event.type==pygame.QUIT:
                #sys.exit()
                pass
        pygame.display.flip()