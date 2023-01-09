# Codility Puzzle
# return the minimal absolute difference when an array is split at various points and the 2 halves are summed and subtracted from each other

def solution(A):
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

print(solution([3,1,2,-4,3]))
print(solution([1000, -1000]))
print(solution([-2,-3,-4,-1]))

# running total solution is too complicated and doesn't work in all situations but working solution above fails on processing time

def solutionplus(A):
    sumofarray = 0
    for item in A:
        sumofarray += abs(item)
    print(A, sum(A), sumofarray)
    
    minimum_difference = float('inf')
    
    running_total = 0
    for number in range(0, len(A)):
        print(A[number])
        running_total + A[number]
        print('running total', running_total)
        posInt = abs(running_total)
        #diff = (sum(A) - running_total) - running_total
        
        firstslice = posInt
        secondslice = sumofarray - posInt
        
        diff = abs(firstslice - secondslice)
        print('firstslice', firstslice, ' - secondslice', secondslice, ' = diff', diff)
        if diff < minimum_difference:
            minimum_difference = diff

    return 'minimum difference is ', minimum_difference

#print(solutionplus([3,1,2,4,3]))
#print(solutionplus([1000, -1000]))
#print(solutionplus([-2,-3,-4,-1]))