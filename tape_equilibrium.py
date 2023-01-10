# Codility Puzzle
# return the minimal absolute difference when an array is split at various points and the 2 halves are summed and subtracted from each other

def solution(A):
    print(A)
    minimum_difference = float('inf')
    total = sum(A)
    print(total)
    for number in range(1, len(A)):
        x = sum(A[0:number])
        diff = abs((total - x) - x)
        if diff < minimum_difference:
            minimum_difference = diff
    #if minimum_difference == 0:
        #return minimum_difference
    return 'minimum difference is ', minimum_difference

print(solution([3,1,2,4,3]))
print(solution([1000, -1000]))
print(solution([-2,-3,-4,-1]))
print(solution([3,-1,2,-4,3]))

#solution is correct but fails on time