'''
create a script with multiple processes, each should generate a random number
try to get the result from a queue
'''

import multiprocessing
from collections import defaultdict
from random import randint

def func1(queue):
    r = randint(1,1000)
    

def main():
    results = multiprocessing.Queue()
    