#find smallest, find largest, create a range, cross reference

def solution(a):
    length = len(a)
    if length == 0:
        return 1
    elif length > 0:
        for item in range(1, length+2):
            if item not in a:
                result = item
                return result
                


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
