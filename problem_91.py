from heapq import *

def minimum_cost_to_connect_ropes(ropeLengths):
  result = 0
  min_heap = []
  for rope in ropeLengths:
    heappush(min_heap, rope)

  while len(min_heap):
    if len(min_heap) > 1:
      rope1 = heappop(min_heap)
      rope2 = heappop(min_heap)
      merged = rope1 + rope2
      heappush(min_heap, merged)
      result += merged
    else:
      rope = heappop(min_heap)

  return result

def main():

  print("Minimum cost to connect ropes: " +
          str(minimum_cost_to_connect_ropes([1, 3, 11, 5])))
  print("Minimum cost to connect ropes: " +
        str(minimum_cost_to_connect_ropes([3, 4, 5, 6])))
  print("Minimum cost to connect ropes: " +
        str(minimum_cost_to_connect_ropes([1, 3, 11, 5, 2])))

main()

