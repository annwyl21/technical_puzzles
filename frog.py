# Codility
# Count minimal number of steps from x to y
# x - start, y - end d - distance

# A small frog wants to get to the other side of the road. 
# The frog is currently located at position X and wants 
# to get to a position greater than or equal to Y. 
# The small frog always jumps a fixed distance, D.
# Count the minimal number of jumps that 
# the small frog must perform to reach its target.

import math

def solution(x, y, d):
    result = math.ceil((y-x)/d)
    return result

print(solution(10, 85, 30))

# Solution minus start point (x) from end point (y) and divide that by the measurement of each step (d).

def solution1(x,y,d):
    remainder = (y-x)%d
    result = (y-x)/d
    if remainder != 0:
        result = result +1
    return int(result)

print(solution1(10, 85, 30))

# Solution uses the solution above but accounts for non-integer results and handles that situation.
