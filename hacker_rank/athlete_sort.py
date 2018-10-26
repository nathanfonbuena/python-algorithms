#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    k = int(input())
     
    def key_sort(elem):
        return elem[k]
    
    arr.sort(key=key_sort)
    new_arr = []
    for i in arr: 
        new_arr.append(["".join(str(j)) for j in i])
        
    for j in new_arr:
        print(" ".join(j))


'''
sample input 

5 3
10 2 5
7 1 0
9 9 9
1 23 12
6 5 9
1

'''