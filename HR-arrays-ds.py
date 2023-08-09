#https://www.hackerrank.com/challenges/arrays-ds/problem
# my submission: https://www.hackerrank.com/challenges/arrays-ds/submissions/code/340145097
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'reverseArray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY a as parameter.
#

def reverseArray(a):
    # Write your code here
    
    return [arr[len(arr) - 1 - index] for index in range(len(arr))]

    # seems simple, feels clumsy to me.
    # make a new array
    # loop through old arr
    # as we iterate, put index[i] i units away from the end of the array (length - i)
    #so index 0 will be at the end (length - 0 = length)
    # etc (index 1 will be (length - 1 = length -1))
    # space complexity is an issue here because we are always pushing to the front. If I revisit this I would want to rework this so that we start at the end of the arr legnth and start from the beggining of the new array. 

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    res = reverseArray(arr)

    fptr.write(' '.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
