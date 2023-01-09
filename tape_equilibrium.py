# Codility Puzzle
# return the minimal absolute difference when an array is split at various points and the 2 halves are summed and subtracted from each other

def solution(A):
    minimum_difference = float('inf')
    for number in range(1, len(A)):
        x = sum(A[0:number])
        y = sum(A) - x   
        diff = abs(y - x)
        if diff < minimum_difference:
            minimum_difference = diff
    return 'minimum difference is ', minimum_difference

print(solution([3,1,2,4,3]))
print(solution([1000, -1000]))

