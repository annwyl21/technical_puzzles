# Codility Puzzle
# How many distinct numbers are in a given array?

def solution(A):
    #print(A)
    ArrayB = []
    for num in A:
        ArrayB.append(abs(num))
    #print(ArrayB)
    dictionary_from_range  = dict.fromkeys(ArrayB, True)
    return len(dictionary_from_range)

print(solution([-5,1,5]))

#Solution makes the array positive then removes duplicates by converting to a dictionary before counting the length of the dictionary