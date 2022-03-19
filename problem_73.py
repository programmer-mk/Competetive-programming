from heapq import *

def find_Kth_smallest(lists, k):
  number = -1
  # TODO: Write your code here
  min_heap = []
  for idx, temp_lst in enumerate(lists):
    heappush(min_heap, (temp_lst[0], idx))
    lists[idx] = lists[idx][1:]

  counter = 1
  while len(min_heap):
    value, index = heappop(min_heap)
    if counter == k:
      number = value
      break
    else:
      curr_lst = lists[index]
      heappush(min_heap, (curr_lst[0], idx))
      lists[index] = lists[index][1:]
      counter += 1

  return number

def main():
  print("Kth smallest number is: " +
        str(find_Kth_smallest([[2, 6, 8], [3, 6, 7], [1, 3, 4]], 5)))


main()
