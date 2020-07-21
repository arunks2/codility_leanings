# O(N+M) 100% score
def solution(N, A):
    # write your code in Python 3.6
    # print(N,A)
    l = [0]*N
    
    maximum = 0
    max_update = 0
    
    for a in A:
        if 1 <= a <= N:
            if maximum > l[a-1]:
                l[a-1] = maximum
                
            l[a-1] += 1
            max_update = max_update if max_update > l[a-1] else l[a-1]
        else:
            maximum = max_update
    
    for j in range(N):
        if l[j] < maximum:
            l[j] = maximum
    return l

# O(N+M) 88% Score

def solution(N, A):
    # write your code in Python 3.6
    # print(N,A)
    l = [0]*N
    
    maximum = 0
    for i in range(len(A)):
        if A[i] >= 1 and A[i] <= N:
            l[A[i]-1] = l[A[i]-1] + 1
            maximum = maximum if maximum > l[A[i]-1] else l[A[i]-1]
        elif A[i] == N+1:
            l = [maximum]*N
    return l 