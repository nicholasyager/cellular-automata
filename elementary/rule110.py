#!/usr/bin/python2

import numpy
import pygame.surfarray as surfarray
import pygame
import random
import sys

def main():
    print("Running.")
    
    pygame.init()

    modes = pygame.display.list_modes()
    width, height = modes[0]

    size = width, height
    white = 255, 255, 255
    black = 0, 0, 0

    screen = pygame.display.set_mode(size)

    tick = 0

    # Generate the initial generation
    world = numpy.zeros((width,height,1), dtype=int)
    render = numpy.zeros((width,height,3), dtype=int)
    for index in range(0,width-1):
        life = random.randint(0,1)
        if life == 1:
            render[index,tick] = (0,0,0)
            world[index,tick] = 1
        else:
            render[index,tick] = (255,255,255)
            world[index,tick] = 0

    # Generate the initial world

    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
        
        # Evaluate the current array
        life = 0
        for index in range(0,width-1):
            pre = index - 1
            suc = index + 1
            if pre < 0:
                pre = width-1
            if suc >= width:
                suc = 0

            pattern = 0
            if world[pre,tick] == 1:
                pattern += 100
            if world[index,tick] == 1:
                pattern += 10
            if world[suc,tick] == 1:
                pattern += 1

            if tick + 1 == height:
                new_tick = 1
            else:
                new_tick = tick+1

            if pattern in [110,101,11,10,1]:
                render[index,new_tick] = (0,0,0)
                world[index,new_tick] = 1
                life += 1
            else:
                render[index,new_tick] = (255,255,255)
                world[index,new_tick] = 0
           
        
        # Render
        surfarray.blit_array(screen,render)
        pygame.display.update()
        tick += 1
        if life == 0:
            sys.exit()
            
        if tick == height:
            tick = 1



if __name__ == "__main__":
    main()

