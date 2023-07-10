#https://www.hackerrank.com/challenges/one-week-preparation-kit-plus-minus/problem
#my submission: https://www.hackerrank.com/challenges/one-week-preparation-kit-plus-minus/submissions/code/335337524
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    negs = 0
    pos = 0
    zeros = 0
    
    for i in arr:
       
        if i < 0:
            negs += 1
        elif i > 0:
            pos += 1
        else:
            zeros += 1
            
    total = len(arr)
    neg_ratio = "{:.6f}".format(negs / total)
    pos_ratio = "{:.6f}".format(pos / total)
    zero_ratio = "{:.6f}".format(zeros / total, 6)
    print(pos_ratio)
    print(neg_ratio)
    print(zero_ratio)

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
