#!/bin/python3

import math
import os
import random
import re
import sys

def repeatedString(s, n):
    occurrences_a = s.count("a")
    return occurrences_a*(n//len(s)) + s[0:n%len(s)].count("a")

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()

