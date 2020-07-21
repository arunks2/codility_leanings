# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(X, A):
    # write your code in Python 3.6
    covered = [False]*X
    uncovered = X
    for i in range(len(A)):
        if A[i] <=0 or A[i] > X:
            return -1
        if covered[A[i]-1] == False:
            covered[A[i]-1] = True
            
            uncovered -= 1
            
            if uncovered == 0:
                return i
    return -1