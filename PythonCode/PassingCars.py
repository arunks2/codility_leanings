# @Author : Arun Sharma
# @problem statement : https://app.codility.com/programmers/lessons/5-prefix_sums/passing_cars/

def solution(A):
    # write your code in Python 3.6
    count = 0
    zeros = 0
    for a in A:
        if a == 0:
            zeros += 1
        elif a == 1:
            count += zeros
            if count > 1000000000:
                return -1
    return count