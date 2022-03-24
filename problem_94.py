from heapq import heappush, heappop

def find_k_largest_pairs(nums1, nums2, k):
  result = []
  min_heap = []
  for i in range(min(len(nums1), k)):
    for j in range(min(len(nums2), k)):
      if len(min_heap) < k:
        heappush(min_heap, (nums1[i]+nums2[j],i,j))
      else:
        if nums1[i] + nums2[j] > min_heap[0][0]:
          heappop(min_heap)
          heappush(min_heap, (nums1[i]+nums2[j],i,j))
        else:
          break
  
  result =  [[nums1[tup[1]], nums2[tup[2]]] for tup in min_heap]
  return result


def main():
  print("Pairs with largest sum are: " +
        str(find_k_largest_pairs([9, 8, 2], [6, 3, 1], 3)))


main()
