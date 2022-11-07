#task frog trying to cross a river jumping on falling leaves
def solution(x, a):
    steps = range(x+1)
    step_count = 0
    dictionary_from_steps  = dict.fromkeys(steps, False)
    dictionary_from_steps[0] = True
    print(dictionary_from_steps)
    for num in a:
        if num in dictionary_from_steps.keys():
            dictionary_from_steps[num] = True
            print(dictionary_from_steps)
            step_count = step_count +1
            print(step_count)
        if all(value == True for value in dictionary_from_steps.values()):
            return step_count-1

print(solution(5, [1, 3, 1, 4, 2, 3, 5, 4]))