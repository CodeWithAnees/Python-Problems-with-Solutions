#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
counted_list = list()
final_list = list()


def sockMerchant(n, ar):
    make_set = set(ar)
    for i in make_set:
        count_i = ar.count(i)
        counted_list.append(count_i)
    for j in counted_list:
        res = j//2
        final_list.append(res)
    return sum(final_list)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
