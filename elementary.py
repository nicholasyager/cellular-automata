#!/usr/bin/python2

"""
elementary.py

A general simulator that will simulate a elementary cellular automata using any 
of the 256 rule sets available to elementary automata.

Usage:                                                                          
    elementary.py <rule>
                                                                                 
Options:
    rule: An interger rule that is the decimal representation of the 16 bit
          binary rule set. The default is Rule 110.
"""


import numpy
import pygame.surfarray as surfarray
import pygame
import random
import getopt
import sys

class RuleError(Exception):
    def __init__(self,value):
        self.value = value
    def __str__(self):
        return repr(self.value)

def parseRule(rule_number):
    """
    The parseRule function takes a integer rule number, and converts it into
    a list of patterns which will result in the colonization of a new cell.

    Accepts:

        rule_number: An integer between 0 and 255.

    Returns:

        rules: A list of patterns which will colonize a new cell.

    Raises:

        RuleError: The rule provided it not a valid rule.
    """

    rule = int(rule_number)

    if rule > 255 or rule < 0:
        raise RuleError(rule)

    # Identify the rule set
    binary_string = "{0:b}".format(rule)
    rule_list = list(binary_string)

    while len(rule_list) < 8:
        rule_list.insert(0,'0')

    rule_truths = [p for p in range(0,len(rule_list)-1) if rule_list[p] == "1"]
    allrules = [111,110,101,100,11,10,1,0]

    return [allrules[i] for i in rule_truths]


def main():

    # Initialize pygame/SDL
    pygame.init()

    modes = pygame.display.list_modes()
    width, height = modes[0]

    # Check options to set the size
    opts, args = getopt.getopt(sys.argv[1:], "w:h:", ["width=", "height="])

    for o, a in opts:
        if o in ("-w", "--width"):
            width = int(a)
        elif o in ("-h", "--height"):
            height = int(a)
   
    # Load the rule set
    rule = int(args[0])

    try:
        rules = parseRule(rule) 
    except RuleError as e:
        print "An exception occurred parsing rule", e.value
        exit(1)


    size = width, height
    white = 255, 255, 255
    black = 0, 0, 0

    # Output information to console.
    print "Rule:", rule
    print "Display size:", width,"x",height


    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("elementary.py Rule " + str(rule))

    tick = 0

    # Generate the initial generation
    world = numpy.zeros((width,height,1), dtype=int)
    render = numpy.zeros((width,height,3), dtype=int)


    render[round(width/2),tick] = (0,0,0)
    world[round(width/2),tick] = 1

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

            if pattern in rules:
                render[index,new_tick] = (0,0,0)
                world[index,new_tick] = 1
                life += 1
            else:
                render[index,new_tick] = (255,255,255)
                world[index,new_tick] = 0
           
        
        # Render
        surfarray.blit_array(screen,render)
        updateRect = pygame.Rect((0,tick-1),(width-1,tick))
        pygame.display.update(updateRect)
        tick += 1
        if life == 0:
            sys.exit()
            
        if tick == height:
            tick = 1



if __name__ == "__main__":
    main()

