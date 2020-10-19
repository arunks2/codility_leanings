# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    A.sort()

    flag = 1
    for index, a in enumerate(A):
        if(index+1 != a):
            flag = 0
            break
        
    return flag