def solution(n, m):
    if m == 0 and n == 0:
        return 0

    if m > n:
        n , m = m , n 
        
    multiple = 1
    divide = 1
    t_n = n+m
    t_m = m
    for _ in range(m):
        multiple *= t_n
        t_n -= 1
        divide *= t_m
        t_m -= 1
        
    return multiple // divide

n = int(input())
m = int(input())
print(solution(n, m))