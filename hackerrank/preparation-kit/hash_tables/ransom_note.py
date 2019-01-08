#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    magazine_words = dict()
    for word in magazine:
        if word not in magazine_words:
            magazine_words[word] = 0
        magazine_words[word]+=1
    can_write = True
    for word in note:
        if word in magazine_words and magazine_words[word]>0:
            magazine_words[word]-=1
        else:
            can_write = False
            break
            
    if can_write:
        print("Yes")
    else:
        print("No")
                

if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)

