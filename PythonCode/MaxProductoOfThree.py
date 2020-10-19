def solution(A):
    # write your code in Python 3.6
    pass
    max1 = -10001
    max2 = -10001
    max3 = -10001
    
    min1 = 10001
    min2 = 10001
    
    
    for a in A:
        if a > max1:
            tmax1 = max1
            max1 = a
            tmax2 = max2
            max2 = tmax1
            max3 = tmax2
            
        elif a > max2:
            tmax2 = max2
            max2 = a
            max3 = tmax2
            
        elif a > max3:
            max3 = a
            
        if a < min1:
            tmin1 = min1
            min1 = a
            min2 = tmin1
        elif a < min2:
            min2 = a
    return max(max1*max2*max3, max1*min1*min2)