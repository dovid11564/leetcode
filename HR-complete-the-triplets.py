# https://www.hackerrank.com/challenges/compare-the-triplets/problem
# my submission: https://www.hackerrank.com/challenges/compare-the-triplets/submissions/code/340897808
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'compareTriplets' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def compareTriplets(a, b):
    # Write your code here
    #we're gonna be comparing each index in an array with it's counterpart in the other. Depending on comparison, we "award" points in another array, which we return

    sol = [0, 0]
    #loop through a
    
    i = 0
    while i < len(a):
        if a[i] == b[i]:
            i += 1
        elif a[i] > b[i]:
            sol[0] += 1
            i += 1
        elif a[i] < b[i]:
            sol[1] += 1
            i += 1           
    return sol
 

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
