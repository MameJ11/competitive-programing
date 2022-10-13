#!/bin/python3

import math
import os
import random
import re
import sys

def countingValleys(steps, path):
    number_of_valleys = 0
    sea_level = 0
    for steps in path:
        if steps == "D":
            sea_level -= 1
        elif steps == "U":
            sea_level += 1
            if sea_level == 0:
                number_of_valleys += 1
    return number_of_valleys 
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()
