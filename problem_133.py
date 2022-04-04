# Note: Proper indentation is required 
# Click HELP above to see examples of handling input/debug/output 
# INPUT: n = input() 
# DEBUG: print(n) 
# OUTPUT: print(result) 

# Write the code to solve the problem below,  
# format the "result" as specified in the problem statement 
# and finally, write the result to stdout 
# IMPORTANT: Remove all debug statements for final submission 


def fill_glasses(total, level, index):
    list = [[0] * (p+1) for p in range(total)]
    
    def fill_glasses_recusive(K, i, j, list):
        if i > total or j > total:
            return

        if list[i][j] + K <= 1.0:
            list[i][j] += K
            return
        else:
            diff = list[i][j] + K - 1.0
            list[i][j] = 1.0
            fill_glasses_recusive(diff/2, i+1, j, list)
            fill_glasses_recusive(diff/2, i+1, j+1, list)
        
    fill_glasses_recusive(total, 0, 0, list)    
    return list[level-1][index-1]
                    
                    
k = int(input())
i = int(input())
j = int(input())
print(fill_glasses(k,i,j))