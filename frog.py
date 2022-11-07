import math

def solution(x, y, d):
    result = math.ceil((y-x)/d)
    return result

print(solution(10, 85, 30))
# x - start, y - end d - distance

def solution1(x,y,d):
    remainder = (y-x)%d
    result = (y-x)/d
    if remainder != 0:
        result = result +1
    return int(result)

print(solution1(10, 85, 30))