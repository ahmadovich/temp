import argparse
import sys 

parsecontainer = argparse.ArgumentParser(description = 'Usage: Arguments.py -r/--radius [radius]')
parsecontainer.add_argument('-r', '--radius',type = float, required = True, metavar = '', help = 'Radius        Radius of cylinder, ex: -r 5')

myargs = parsecontainer.parse_args()

print (myargs.radius)