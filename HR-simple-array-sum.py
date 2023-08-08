# https://www.hackerrank.com/challenges/simple-array-sum/problem
# WIP. Working on solving this recursively. 
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'simpleArraySum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY ar as parameter.
#

def simpleArraySum(ar):
    # Write your code here
    
    i = 0
    sum = 0
    #we make a function that takes in ar, i, and current sum
    def recursive_function(ar, i, sum):
        #base case is if  i >= ar.legnth, return the sum
        if i >= len(ar):
            return sum
        #else we add ar[i] to the current sum
        print(sum)
        sum += ar[i]
        print(sum)
        return recursive_function(ar, i+1, sum)
    
    #and we return function but with new params. 

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = simpleArraySum(ar)

    fptr.write(str(result) + '\n')

    fptr.close()
