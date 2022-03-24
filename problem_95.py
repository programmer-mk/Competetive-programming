from heapq import heappush, heappop

def sort_character_by_frequency(str):
  if not len(str):
    return ""

  result = ""
  occurencies = {}
  max_heap = []
  for c in str:
    if occurencies.get(c):
      occurencies[c] += 1
    else:
      occurencies[c] = 1

  for key in occurencies:
    heappush(max_heap, (-occurencies[key], key))

  while len(max_heap):
    occurs, elem = heappop(max_heap)
    for i in range(-occurs):
      result += elem

  return result

def main():

  print("String after sorting characters by frequency: " +
        sort_character_by_frequency("Programming"))
  print("String after sorting characters by frequency: " +
        sort_character_by_frequency("abcbab"))


main()
