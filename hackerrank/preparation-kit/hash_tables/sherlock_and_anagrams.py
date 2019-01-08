#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sherlockAndAnagrams function below.
def sherlockAndAnagrams(s):
    counts = 0
    for n_words in range(len(s)):
        if n_words > 0:
            seen_substr = list()
            for i in range(len(s)-n_words+1):
                substr = s[i:i+n_words]
                print
                word_count = dict()
                for word in substr:
                    if word not in word_count:
                        word_count[word] = 0
                    word_count[word]+=1
                for substr in seen_substr:
                    if word_count == substr:
                        counts+=1
                seen_substr.append(word_count)
    return counts


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        fptr.write(str(result) + '\n')

    fptr.close()

