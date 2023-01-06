# Codility Puzzle
# return the minimal absolute difference when an array is split at various points and the 2 halves are summed and subtracted from each other

def solution(A):
    min_diff = float('inf')
    sumofarray = 0
    for element in A:
        sumofarray += element
    #print(sumofarray)
    smallsum = 0
    diff = 0
    length = len(A)
    indexlist = range(1, length)
    for number in indexlist:
        breakpoint = number
        initialsection = A[0:breakpoint]
        #print(initialsection)
        for item in initialsection:
            smallsum += item
            #print(smallsum)
        diff = sumofarray - smallsum
        #print(diff)
        #print(min_diff)
        smallsum = 0
        if diff < min_diff:
            min_diff = diff
    return 'minimum difference', min_diff

print(solution([3,1,2,4,3]))