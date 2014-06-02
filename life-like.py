#!/usr/bin/python2
# -*- coding: utf-8 -*-
"""
life-like.py

A script that simulates a life-like cellular automaton using the rules of
Conway's Game of Life.

Usage:                                                                          
    life-like.py
                                                                                 
"""

import os
import random
import time

class World():
    width = 0
    height = 0

    def __init__(self):
        """
        Initial creation of a world. Determine the dimensions of the world and
        populate it accordingy.
        """

        # Create the world
        self.height, self.width = get_terminal_size();

        self.matrix = [[0 for x in range(self.width)] for x in range(self.height)]

        
    def populate(self, p = 0.5):
        """
        Iterate through the world randomly placing life in positions based on
        a probability p.
        """
        for row in range(self.height):
            for col in range(self.width):
                # If the odds are in the position's favor
                if random.uniform(0,1) <= p:
                    # The cell is alive.
                    self.matrix[row][col] = "█"
                else:
                    # The cell is dead.
                    self.matrix[row][col] = " "

    def show(self):
        """
        Print the current world to the console.
        """
        #os.system('cls' if os.name=='nt' else 'clear')
        for row in range(self.height):
            print("".join(self.matrix[row]))

                
    def simulate(self):
        """
        Examine the number of neighbors for each cell and determine if a future
        lifeform will occupy the same space.

        Algorithm:
            1. Choose a cell.
            2. Count its neighbors.
            3. If the cell has 3 neighbors, it lives regardless of current 
               state. If the cell is alive and has 2 neighbors, it lives. 
               Otherwise, the cell is dead. All changes to the world are saved 
               in the next generation matrix "NGM".
            4. Once completed, replace the world with the NGM.
        """
 
        self.NGM = [[0 for x in range(self.width)] for x in range(self.height)]

        for row in range(self.height):
            for col in range(self.width):

                # Setup a basic template for neighbor coordinates.
                neighbors = [ (row - 1, col - 1), (row - 1, col), 
                              (row - 1, col + 1), (row, col + 1),
                              (row + 1, col + 1), (row + 1, col),
                              (row + 1, col - 1), (row, col - 1) ]
                n_neighbors = 0

                for n_row, n_col in neighbors:

                    # Check for bounding errors

                    if n_row < 0:
                        n_row = self.height - 1
                    elif n_row == self.height:
                        n_row = 0

                    if n_col < 0:
                        n_col = self.width - 1
                    elif n_col == self.width:
                        n_col = 0

                    if self.matrix[n_row][n_col] == "█":
                        n_neighbors += 1

                # Determine if there will be life in that cell on the next tick
                if n_neighbors == 3:
                    self.NGM[row][col] = "█"
                elif n_neighbors == 2 and self.matrix[row][col] == "█":
                    self.NGM[row][col] = "█"
                else:
                    self.NGM[row][col] = " "
       
        self.matrix = self.NGM 
    
def main():

    # Clear the terminal
    os.system('cls' if os.name=='nt' else 'clear')

    # Create the world
    world = World()

    # Populate it with life
    world.populate()

    # Simulate the world
    while True:

        world.show()      # Write the current tick
        world.simulate()    # Simulate the next tick


def get_terminal_size(fd=1):
    """
    Returns height and width of current terminal. First tries to get
    size via termios.TIOCGWINSZ, then from environment. Defaults to 25
    lines x 80 columns if both methods fail.

    Arguments:

        fd: File descriptor (default: 1=stdout)

    Returns:
        (width, height):    A tuple containing the width and height of the 
                            terminal window.
    """
    try:
        import fcntl, termios, struct
        hw = struct.unpack('hh', fcntl.ioctl(fd, termios.TIOCGWINSZ, '1234'))
    except:
        try:
            hw = (os.environ['LINES'], os.environ['COLUMNS'])
        except:  
            hw = (25, 80)

    return hw

if __name__ == "__main__":
    main()
