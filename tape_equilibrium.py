# Codility Puzzle
# return the minimal absolute difference when an array is split at various points and the 2 halves are summed and subtracted from each other

def solution(A):
    minimum_difference = float('inf')
    for number in range(1, len(A)):
        x = sum(A[0:number])
        diff = abs((sum(A) - x) - x)
        if diff < minimum_difference:
            minimum_difference = diff
            if minimum_difference == 0:
                return minimum_difference
    return 'minimum difference is ', minimum_difference

#print(solution([3,1,2,4,3]))
#print(solution([1000, -1000]))

def solutionplus(A):
    minimum_difference = float('inf')
    running_total = 0
    for number in range(1, len(A)):
        running_total += A[number]
        #print(x)
        diff = abs((sum(A) - running_total) - running_total)
        #print(diff)
        if diff < minimum_difference:
            minimum_difference = diff
        if minimum_difference == 0:
            return minimum_difference
    return 'minimum difference is ', minimum_difference

print(solutionplus([3,1,2,4,3]))
print(solutionplus([1000, -1000]))