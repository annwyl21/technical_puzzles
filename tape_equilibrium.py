# Codility Puzzle
# return the minimal absolute difference when an array is split at various points and the 2 halves are summed and subtracted from each other

def solution(A):
    print(A)
    minimum_difference = float('inf')
    total = sum(A)
    for number in range(1, len(A)):
        x = sum(A[0:number])
        diff = abs((total - x) - x)
        if diff < minimum_difference:
            minimum_difference = diff
    if minimum_difference == 0:
        return minimum_difference
    return 'minimum difference is ', minimum_difference

print(solution([3,1,2,4,3])) #1
print(solution([1000, -1000])) #2000
print(solution([-2,-3,-4,-1])) #0
print(solution([3,1,2,-4,3])) #1 

# solution loops through the array to sum a slice of the array
# and calculate the minimum absolute difference
# Minimal difference is set at the biggest possible number (infinity) and then replaced by increasingly smaller values
# if minimal difference of 0 is reached, the code returns the 0 result and the loop is broken
# scores 53% on coditlity - solution is correct but fails on the time requirement

def solutionplus(A):
    print(A)
    minimum_difference = float('inf')
    dark = 0
    light = sum(A)
    length = len(A) - 1
    for index in range(0, length):
        light -= A[index]
        dark += A[index]
        diff = abs(dark - light)
        if diff < minimum_difference:
            minimum_difference = diff
    if minimum_difference == 0:
        return minimum_difference
    return 'minimum difference is ', minimum_difference

print(solutionplus([3,1,2,4,3])) #1
print(solutionplus([1000, -1000])) #2000
print(solutionplus([-2,-3,-4,-1])) #0
print(solutionplus([3,1,2,-4,3])) #1 

# solutionplus reduces the time by only passing through the array once
# the sum of the array is gradually reduced by the value of each element
# the absolute difference between the 'light side' (where the sum of the array exists)
# and the 'dark side' (where the value increases by each element incrementally) is calculated
# scores 100% on codility