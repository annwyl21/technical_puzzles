# Codility Puzzle
# return the minimal absolute difference when an array is split at various points and the 2 halves are summed and subtracted from each other

def solution(A):
    min_diff = float('inf')
    smallsum = 0
    bigsum = 0
    diff = 0
    length = len(A)+1
    indexlist = range(0, length)
    for number in indexlist:
        breakpoint = number
        initialsection = A[0:breakpoint]
        #print(initialsection)
        finalsection = A[breakpoint:]
        #print(finalsection)
        for item in initialsection:
            smallsum += item
        for digit in finalsection:
            bigsum += digit
        diff = abs(bigsum - smallsum)
        smallsum = 0
        bigsum = 0
        if diff < min_diff:
            min_diff = diff
    return 'minimum difference', min_diff

print(solution([3,1,2,4,3]))

def solutionplus(A):
    minimum_difference = float('inf')
    x = 0
    y = sum(A) - x
    indexlist = range(1, len(A))
    for number in indexlist:
        initialsection = A[0:number]
        print
        x = sum(initialsection)    
        diff = y - x
        if diff < minimum_difference:
            minimum_difference = diff
    return 'minimum difference is ', minimum_difference

print(solutionplus([3,1,2,4,3]))

