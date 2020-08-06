#!/bin/python3




import math
import os
import random
import re
import sys

# Complete the isBalanced function below.
def isBalanced(s):
    stack = []
    open_close_brackets = {")":"(","}":"{","]":"["}
    open_brackets =  set(["(","{","["])

    for bracket in s:
        if bracket in open_brackets:
            stack.append(bracket)
        else:
            if len(stack)>0:
                last_bracket = stack.pop()
                if open_close_brackets[bracket] != last_bracket:
                    return "NO"
            else:
                return "NO"
    if len(stack)>0:
        return "NO"
    return "YES"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()

