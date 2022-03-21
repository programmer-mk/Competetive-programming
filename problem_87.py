import math


class ArrayReader:

  def __init__(self, arr):
    self.arr = arr

  def get(self, index):
    if index >= len(self.arr):
      return math.inf
    return self.arr[index]


"""
    Time complexity: O(2*log(N))
    Space complexity: O(1)
"""
def search_in_infinite_array(reader, key):
  end = 0
  while reader.get(end) < key:
    end = 2**end

  start = 0
  while(start <= end):
    mid = (start + end) // 2
    if reader.get(mid) == key:
      return mid
    elif reader.get(mid) > key:
      end = mid - 1
    else:
      start = mid + 1

  return -1

def main():
  reader = ArrayReader([4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30])
  print(search_in_infinite_array(reader, 16))
  print(search_in_infinite_array(reader, 11))
  reader = ArrayReader([1, 3, 8, 10, 15])
  print(search_in_infinite_array(reader, 15))
  print(search_in_infinite_array(reader, 200))


main()







