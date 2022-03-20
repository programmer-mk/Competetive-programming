from __future__ import print_function


class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

  def print_list(self):
    temp = self
    while temp is not None:
      print(temp.value, end=" ")
      temp = temp.next
    print()


def reverse_alternate_k_elements(head, k):
  current = head
  previous = None
  reverse = True
  result_head = None
  result_tail = None
  counter = 0
  while current:
    if not reverse:
      if counter == 0:
        result_tail.next = current

      counter += 1
      if counter == k:
        counter = 0
        reverse = True
        result_tail = current
        previous = None
      current = current.next
      
    else:
      # start reversing
      next = current.next
      current.next = previous
      previous = current
      current = next
      counter += 1
      if counter == k:
        reverse = False
        counter = 0
        if not result_head:
          result_head = previous
          result_tail = head
        else:
          temp = result_tail.next
          result_tail.next = previous
          result_tail = temp

  return result_head


def main():
  head = Node(1)
  head.next = Node(2)
  head.next.next = Node(3)
  head.next.next.next = Node(4)
  head.next.next.next.next = Node(5)
  head.next.next.next.next.next = Node(6)
  head.next.next.next.next.next.next = Node(7)
  head.next.next.next.next.next.next.next = Node(8)

  print("Nodes of original LinkedList are: ", end='')
  head.print_list()
  result = reverse_alternate_k_elements(head, 2)
  print("Nodes of reversed LinkedList are: ", end='')
  result.print_list()


main()
