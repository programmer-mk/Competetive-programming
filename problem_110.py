#!/bin/python3

import re
import sys
import math
import random
import os


def longest_subsequence(A, B, idx1, idx2, dp):
    print(f"indicies: {idx1}, {idx2}")
    if idx1 == len(A) or idx2 == len(B):
        return ""
    elif dp[idx1][idx2] != "-":
        return dp[idx1][idx2]
    elif A[idx1] == B[idx2]:
        dp[idx1][idx2] = A[idx1] + longest_subsequence(A, B, idx1+1, idx2+1, dp)
    else:
        first = longest_subsequence(A, B, idx1, idx2+1, dp)
        second = longest_subsequence(A, B, idx1+1, idx2, dp)
        if len(first) > len(second):
            dp[idx1][idx2] = first
        else:
            dp[idx1][idx2] = second
    
    return dp[idx1][idx2]
    
    

def solve(A,B):
    N = len(A)
    M = len(B)
    dp = [['-' for _ in range(M)] for _ in range(N)]
    print(dp)
    ls = longest_subsequence(A, B, 0, 0, dp)
    print(f'Longest subsequence: {ls}')
    if len(ls) < M / 3:
        return "NO"
    else:
        return "YES"
        

if __name__ == '__main__': 
    A = "areakefvowledfriyjejqnnaeqheoh"
    B = "npnkmawey"
    outcome = solve(A, B)
     
    print(outcome)
