# Codility Puzzle - Cyclic Rotation
# rotate an array right by a specified number of places

def solution(A, K):
    my_array = A
    if len(my_array) > 0 and K > 0:
        for n in range(K):
            my_array.insert(0, my_array[-1])
            my_array.pop(-1)
    return my_array

print(solution([1,2,3,4,5], 0))
print(solution([1,2,3,4,5], 3))
print(solution([], 3))

# Solution checks 2 conditions: the array is not empty and the rotation is bigger than 0
# then inserts the number in last position onto the beginning,
# then pops the number off the end, 
# which shifts the whole array right by 1 place. 
# This is repeated using a loop for a specified number of times.
# The original array is changed.