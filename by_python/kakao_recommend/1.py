from itertools import combinations
import math
import os
import random
import re
import sys

# Complete the 'diverseDeputation' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER m
#  2. INTEGER w
#


def diverseDeputation(m, w):
    man_list = list(range(m))
    woman_list = list(range(w))
    ret = len(list(combinations(man_list, 1))) * len(list(combinations(woman_list, 2)))
    ret += len(list(combinations(man_list, 2))) * len(list(combinations(woman_list, 1)))
    return ret


if __name__ == "__main__":
    m = 3
    w = 1
    print(diverseDeputation(m, w))
