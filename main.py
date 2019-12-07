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
dt = .5
size = width, height = 500, 500
res = 50
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
    numRip = len(ripples)
    if numRip == 0:
        numRip = 1
    for i in range(res):
        for j in range(res):
            height = 0
            for rip in ripples:
                height += rip.height(i*pixelSize[0], j*pixelSize[1], t)
            height /= numRip
            color = magToColor(height)
            rect = pygame.Rect(i*pixelSize[0], j*pixelSize[1], pixelSize[0], pixelSize[1])
            pygame.draw.rect(screen, color, rect)

    

if __name__=="__main__":
    pygame.init()
    pygame.font.init()
    f = pygame.font.SysFont("", 48)
    screens = []
    texts = []
    texts.append(f.render("You asked for", True, (0,255,0)))
    texts.append(f.render("a green dance that took", True, (0,255,0)))
    texts.append(f.render("between 15 minutes and", True, (0,255,0)))
    texts.append(f.render("15 hours to create.", True, (0,255,0)))
    texts.append(f.render("", True, (0,255,0)))
    texts.append(f.render("15 minutes didn't seem like", True, (0,255,0)))
    texts.append(f.render("that much effort.", True, (0,255,0)))
    texts.append(f.render("", True, (0,255,0)))
    texts.append(f.render("This class deserves more", True, (0,255,0)))
    texts.append(f.render("than just that.", True, (0,255,0)))
    
    screens.append(texts)
    
    texts = []
    texts.append(f.render("You were fantastic, ola!", True, (0,255,0)))
    texts.append(f.render("", True, (0,255,0)))
    texts.append(f.render("I loved your lectures", True, (0,255,0)))
    texts.append(f.render("and the way you would", True, (0,255,0)))
    texts.append(f.render("present things.", True, (0,255,0)))
    texts.append(f.render("", True, (0,255,0)))
    texts.append(f.render("I have enjoyed many of", True, (0,255,0)))
    texts.append(f.render("my classes here at Duke,", True, (0,255,0)))
    texts.append(f.render("but CS 201 has been", True, (0,255,0)))
    texts.append(f.render("my favorite by far, so far.", True, (0,255,0)))
    
    screens.append(texts)
    
    texts = []
    texts.append(f.render("So here's my green dance.", True, (0,255,0)))
    texts.append(f.render("", True, (0,255,0)))
    texts.append(f.render("There's something pleasing", True, (0,255,0)))
    texts.append(f.render("about ripples in a lake, about", True, (0,255,0)))
    texts.append(f.render("watching one small action", True, (0,255,0)))
    texts.append(f.render("spread to the rest of the world.", True, (0,255,0)))
    texts.append(f.render("", True, (0,255,0)))
    texts.append(f.render("Also, this is a program I've", True, (0,255,0)))
    texts.append(f.render("wanted to write for a while,", True, (0,255,0)))
    texts.append(f.render("and this seemed like ", True, (0,255,0)))
    texts.append(f.render("the right time to write it.", True, (0,255,0)))

    screens.append(texts)
    
    texts = []
    texts.append(f.render("Enjoy!", True, (0,255,0)))
    texts.append(f.render("", True, (0,255,0)))
    texts.append(f.render("Code can be found at:", True, (0,255,0)))
    texts.append(f.render("github.com/puzzler7/PyRipple", True, (0,255,0)))
    
    
    screens.append(texts)
    
    
    
    screen = pygame.display.set_mode(size)
    t = 0
    screen.fill(magToColor(0))
    pressed = False
    
    
    for scr in screens:
        while True:
            screen.fill((0,0,0))
            for i, text in enumerate(scr):
                screen.blit(text, (0,40*i))
            for event in pygame.event.get():  #praxis stuff
                if event.type==pygame.QUIT:
                    pygame.quit()
                    sys.exit("Program closed")
            mouse = pygame.mouse.get_pressed()
            if mouse[0]:
                if not pressed:
                    pressed = True
                    break
            else:
                pressed = False
            pygame.display.flip()
            
    
    
    while True:
        for event in pygame.event.get():  #praxis stuff
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit("Program closed")
        mouse = pygame.mouse.get_pressed()
        if mouse[0]:
            if not pressed:
                pressed = True
                pos = pygame.mouse.get_pos()
                rip = Ripple(pos[0], pos[1], t)
                ripples.append(rip)
        else:
            pressed = False
        draw()

        

        t += dt
        
        pygame.display.flip()
        