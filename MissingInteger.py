def solution(A):
    # write your code in Python 3.6
    
    missing = [0]*1000001
    for a in A:
        if a> 0:
            missing[a] += 1
    
    missed = len(missing)
    for m in range(1,len(missing)):
        if missing[m] == 0:
            missed = m
            break
            
    return missed