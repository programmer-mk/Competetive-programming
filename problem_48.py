def square_num(num):
  sum = 0
  while(num > 0):
    digit = num % 10
    sum += digit**2
    num = int(num / 10)
  return sum


def find_happy_number(num):
  # TODO: Write your code here
  slow, fast = num, num
  print('num:'+ str(num))
  while True:
    slow = square_num(slow)
    fast = square_num(square_num(fast))
    if slow == fast:
      break
  return fast == 1


def main():
  print(find_happy_number(23))
  print(find_happy_number(12))

main()
