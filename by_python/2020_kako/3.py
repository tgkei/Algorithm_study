#!/bin/python3

import math
import os
import random
import re
import sys
from collections import OrderedDict

# Complete the climbingLeaderboard function below.
def climbingLeaderboard(scores, alice):
    ret = []
    idx = 0
    new_score = list()
    new_alice = OrderedDict()

    for score in scores:
        if new_score and new_score[-1] == score: continue
        new_score.append(score)

    th = len(new_score)

    for score in alice:
        if score in new_alice:
            new_alice[score] += 1
        else:
            new_alice[score] = 1

    new_alice = list(new_alice.items())

    for score, num in new_alice:
        while th >= 0 and score > new_score[th-1]:
            th-=1
        if th == -1:
            for _ in range(num):
                ret.append(1)
        elif score < new_score[th-1]:
            for _ in range(num):
                ret.append(th+1)
        elif score == new_score[th-1]:
            for _ in range(num):
                ret.append(th)
    
    return ret

if __name__ == '__main__':
    scores_count = int(input())

    scores = list(map(int, input().rstrip().split()))

    alice_count = int(input())

    alice = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(scores, alice)

    print(result)