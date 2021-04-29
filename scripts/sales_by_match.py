#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#

def sockMerchant(n, ar):
    # Write your code here
    total_pairs = {}
    for c in ar:
        total_pairs[c] = total_pairs[c] + 1 if c in total_pairs else 1
    
    pairs = 0 
    
    for color in total_pairs:
        if total_pairs[color] >= 2:
            pairs += math.floor(total_pairs[color] /2 )

    return pairs        
            
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
