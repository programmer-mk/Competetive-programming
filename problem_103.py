def search_min_diff_element(arr, key):
  N = len(arr)
  left, right = 0, N-1
  while left <= right:
    mid = (left + right) // 2
    if arr[mid] == key:
      return 0
    elif arr[mid] > key:
      right = mid-1
    else:
      left = mid+1

  if left == N:
    return abs(arr[N-1] - key)

  if right == -1:
    return abs(arr[0] - key)

  return min(abs(arr[left] - key), abs(arr[right] - key))


def main():
  print(search_min_diff_element([4, 6, 10], 7))
  print(search_min_diff_element([4, 6, 10], 4))
  print(search_min_diff_element([1, 3, 8, 10, 15], 12))
  print(search_min_diff_element([4, 6, 10], 17))


main()
