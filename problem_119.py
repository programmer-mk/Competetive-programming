from copy import deepcopy
import math

def print_result_list(list):
    for num in list:
        print(num)


def solve_recursive(array, n, number, previous, k, steps, result):
    if k == steps:
        return True, result
        
    for num in array:
        if num > number and num != previous:
            temp_res = deepcopy(result)
            temp_res.append(num)
            founded, result2 = solve_recursive(array, n, num-number, num, k+1, steps, temp_res)
            if founded:
                return True, result2
    
    return False, []

def solve(array, n, steps):
   
    founded = False
    for num in array:
        result = [num]
        founded, result = solve_recursive(array, n, num, math.inf, 1, steps, result)
        if founded:
            print_result_list(result)
            founded = True
            break
    
    if not founded:
        print("Not Possible")

n = int(input())
steps = int(input())
array = list(map(int, input().strip().split(' ')))
solve(array, n, steps)
