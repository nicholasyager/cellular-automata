cellular-automata
=====

A series of python scripts that run various type of cellular automata.

Requirements:
-----
 - Python2
 - Pygame
 - Numpy

Elementary.py
-----
A general simulator that will simulate a elementary cellular automata using any
of the 256 rule sets available to elementary automata.


    elementary.py [--width=<width> --height=<height>] <rule>

    Usage:

        elementary.py 110
        elementary.py --width=800 --height=600 126

    Options:
        rule: An interger rule that is the decimal representation of the 16 bit 
              binary rule set. The default is Rule 110.

