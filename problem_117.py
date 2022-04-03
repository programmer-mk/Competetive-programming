def is_armstrong(number):
    sum_digit_cubes = 0
    n = number
    while n > 0:
        digit = n % 10
        sum_digit_cubes += digit ** 3
        n = n // 10
        
    if sum_digit_cubes == number:
        return "Yes"
    else:
        return "No"

n = int(input())
print(is_armstrong(n)) 