# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    diff_array = []
    start_sum = A[0]
    big_num = 99999999999
    end_sum = big_num
    end_sum_array = [big_num]
    last_num = A[len(A)-1]
    minimum = 99999999999
    start_sum_array = [start_sum]
    for i in range(1,len(A)-1):
        start_sum += A[i]
        start_sum_array.append(start_sum)
        end_sum -= A[i]
        end_sum_array.append(end_sum)
    
    real_sum = big_num - end_sum_array[len(end_sum_array)-1] + last_num
    
    for j in range(0, len(end_sum_array)):
        previous_value = end_sum_array[j]
        num = end_sum_array[j]
        end_sum_array[j] = previous_value - big_num + real_sum
        diff = abs(start_sum_array[j] - end_sum_array[j])
        minimum = diff if diff < minimum  else minimum
    return minimum