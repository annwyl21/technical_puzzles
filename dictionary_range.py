#Codility
#Missing element in permutation

def solution(a):
    dictionary_from_range  = dict.fromkeys(a, True)
    print(range(1, len(a)+2))
    for num in range(1, len(a)+2):
        if num not in dictionary_from_range:
            return num

print("4 - non-sequential, missing in the middle")
print(solution([1, 2, 6, 5, 3]))
print("5 - missing at the end")
print(solution([1, 2, 4, 3]))
print("1 - 1 element in array")
print(solution([2]))
print("3 - 2 elements in array")
print(solution([1,2]))
print("1 - empty array")
print(solution([]))

#Solution converts the given array into a dictionary because it is faster to look thing up (find the missing element) in a dictionary than a list.
#The number in the array is used as a the key and the value true is assigned to each number because I do not need the values, just a faster (efficient) lookup.
#A loop checks the values in a range against the dictionary and returns the missing number or returns the next number in the permutation.
