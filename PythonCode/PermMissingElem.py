# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    N = len(A)
    sum_array = sum(A)
    real_sum = int((N+1)*(N+2)/2)
    return real_sum - sum_array