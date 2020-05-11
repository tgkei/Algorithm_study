#!/bin/python3

import math
import os
import random
import re
import sys

# def maximumProfit(price):
#     ordered_map = dict()
#     ret = 0
    
#     for idx, each in enumerate(price):
#         ordered_map[each] = idx

#     ordered_map = sorted(ordered_map.items(), reverse = True)

#     prev_idx = 0

#     for maximum, idx in ordered_map:
#         if idx < prev_idx: continue
#         for each in price[prev_idx: idx]:
#             if each != maximum:
#                 ret -= each
#         ret += ((idx-prev_idx) * maximum)
#         prev_idx = idx + 1
    
#     return ret

def maximumProfit(price):
    ret = 0
    maximum = price[-1]
    for each in reversed(price[:-1]):
        if maximum < each :
            maximum = each
            continue
        ret += (maximum - each)

    return ret

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        price = list(map(int, input().rstrip().split()))

        profit = maximumProfit(price)
        print(profit)
        #fptr.write(str(profit) + '\n')

    #fptr.close()
