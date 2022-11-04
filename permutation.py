#Codility
#Is array a permutation? Yes or No answer

def solution(A):
    length = len(A)
    myset = set((A))
    A.sort()
    if length == len(myset) and A[-1] == length:
        return 1
    else:
        return 0

print(solution([1,2,3,4]))
print(solution([0,5,6]))
print(solution([10,2,5,4,5,6,7,8,1,9]))

#Solution converts the array into a set because a set can not have duplicates.
#Then sorts the array.
#The code the checks 2 conditions:
#1. the length of the set is the the same as the length of the array, i.e. it had no duplicates,
#2. the last digit of the sorted array is the same as the length of the array.
#A permutation will return a Yes (1) response and if the array is not a permutation a No (0) is returned.
