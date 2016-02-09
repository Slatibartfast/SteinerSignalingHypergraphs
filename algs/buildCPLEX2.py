# buildCPLEX2.py
#
#
# Barney Potter
#
# File for converting a directed signaling hypergraph
# (constructed using the halp package) into a .lp file
# that can be solved using CPLEX solver.
#
#
#

import sys

def makefile(name):
    print('Creating new text file')

    filename = name+'.txt'  # Name of text file coerced with +.txt

    try:
        file = open(filename,'a')   # Trying to create a new file or open one
        file.close()

    except:
        print('Something went wrong! Can\'t tell what?')
        sys.exit(0) # quit Python



makefile()
