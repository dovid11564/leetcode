#https://www.hackerrank.com/challenges/time-conversion/problem
#my submission: https://www.hackerrank.com/challenges/one-week-preparation-kit-time-conversion/submissions/code/335638668
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
   
    if "AM" in s:
        first_two = s[:2]
        print(first_two)
        if first_two == "12":
          new_s = s.replace(s[:2], "00")
          return(new_s.replace('AM', ''))
        return s.replace('AM', '')
    elif "PM" in s:
        first_two = s[:2]
        first_conv = int(first_two)
        sec_conv = first_conv + 12
        third_conv = str(sec_conv)
        fourth_conv = s.replace(first_two, third_conv)
        fifth_conv = fourth_conv.replace("PM", "")
        return fifth_conv
        
   

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
