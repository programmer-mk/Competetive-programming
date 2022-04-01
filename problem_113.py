"""
    Glider tests cannot support different order of result items,
    order in tests is pretty much random.Leave comment on platform
    for Glider team to improve that.
"""



def search(array, i, j, result):
    left = j
    right = len(array) - 1
    while left < right:
        if array[left] + array[right] + array[i] == 0:
            result.add((array[left],array[right],array[i]))
            break
        elif array[left] + array[right] + array[i] > 0:
            right -= 1
        else:
            left += 1  
        

def solution(array):
    N = len(array)
    if N < 3:
        return None
       
    result = set()
    array.sort()
    for i in range(N-2):
        for j in range(i+1, N-1):
            search(array, i, j, result)
        
    for comb in result:
        print(comb[0])
        print(comb[1])
        print(comb[2])
    return result

n = int(input().strip())
array = list(map(int, input().strip().split(' ')))
solution(array)