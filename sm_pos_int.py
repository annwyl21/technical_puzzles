# Codility Puzzle Smallest Positive Integer
# Find the smallest positive integer missing from an array

def solution(A):
    dictfromlist = dict.fromkeys(B, True)
    for number in range(1, 1000000):
        if number not in dictfromlist:
            return number

print(solution([1,3,6,4,1,2])) #5
print(solution([1,2,3])) #4
print(solution([-1,-3])) #2