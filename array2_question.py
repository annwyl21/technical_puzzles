# Codility Puzzle
# Locate the value in an array that does not have a match/ pair/ snap ?

def solution(A):
    frequency = {}
    for num in A:
        if num not in frequency:
            frequency[num] = 0
        frequency[num] += 1
    #print(frequency)
    for key, value in frequency.items():
        if value %2 != 0:
            result = key
    return result

print(solution([9,3,9,3,9,7,9]))

# Solution creates an empty dictionary called 'frequency',
# loops through the given array to add novel numbers to the dictionary
# and count the number of times they appear.
# The code then looks through the dictionary to find the item that appears only once
# and returns that item.
