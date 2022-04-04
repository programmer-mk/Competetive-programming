# Note: Proper indentation is required 
# Click HELP above to see examples of handling input/debug/output 
# INPUT: n = input() 
# DEBUG: print(n) 
# OUTPUT: print(result) 

# Write the code to solve the problem below,  
# format the "result" as specified in the problem statement 
# and finally, write the result to stdout 
# IMPORTANT: Remove all debug statements for final submission 


def coin_change(k, curr_sum, array, total, curr_state, result_set):
    if curr_sum > k:
        return
    elif curr_sum == k:
        result_set.add("".join(sorted(curr_state)))
        return
    else:
        for num in array:
            coin_change(k, curr_sum+num, array, 0, curr_state+str(num), result_set)

    return


n = int(input())
array = input().split(" ")
k = int(input())
result_set = set()
result = coin_change(k, 0, [int(num) for num in array], 0, "", result_set)
print(len(result_set))
