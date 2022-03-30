from heapq import heappush, heappop

class KthLargestNumberInStream:
  def __init__(self, nums, k):
    self.min_heap = []
    for idx, num in enumerate(nums):
      if idx < k:
        heappush(self.min_heap, num)
      else:
        if self.min_heap[0] < num:
          heappop(self.min_heap)
          heappush(self.min_heap, num)
    self.k = k

  def add(self, num):
    if len(self.min_heap) < self.k:
        heappush(self.min_heap, num)
    else:
      if self.min_heap[0] < num:
        heappop(self.min_heap)
        heappush(self.min_heap, num)

    return self.min_heap[0]

def main():

  kthLargestNumber = KthLargestNumberInStream([3, 1, 5, 12, 2, 11], 4)
  print("4th largest number is: " + str(kthLargestNumber.add(6)))
  print("4th largest number is: " + str(kthLargestNumber.add(13)))
  print("4th largest number is: " + str(kthLargestNumber.add(4)))


main()

