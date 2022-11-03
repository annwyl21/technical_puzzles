# Codility Puzzle
# Find the binary gap - "A binary gap within a positive integer N is any maximal sequence of consecutive zeros that is surrounded by ones at both ends in the binary representation of N"

def solution(N):
    binary_string = bin(N)
    binary_string = binary_string[2:]
    count = 0
    largest_count = 0
    for item in binary_string:
        if item == '0':
            count = count +1
        elif item == '1':
            if count > largest_count:
                largest_count = count
            count = 0
    return "Number {num}, Binary {binary}, Longest string of 0's is {lc}".format(num = N, binary = binary_string, lc = largest_count)
    
#print(solution(32))
print(solution(5000))

# Solution turns the given number into a string of binary.
# Slice off the first 2 digits since the binary conversion adds 0b to the start of the string. 
# Sets up two zero-ed counters and loops over the string to count the number of consecutive zero's.
# Stores that count as the largest count if it is larger than the number already stored.
# Returns the largest number which is the length of the longest string.
