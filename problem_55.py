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


def reverse_every_k_elements(head, k):
  # TODO: Write your code here
  if k < 2:
    return head

  current = head
  previous = None
  previous_tail = None
  step = 0
  while(current):
    i = 0
    start = current
    while(current and i < k):
      next = current.next
      current.next = previous
      previous = current
      current = next
      i += 1

    if step == 0:
      head = previous
    
    if not previous_tail:
      previous_tail = start
    else:
      previous_tail.next = previous
      previous_tail = start
    previous = None
    step += 1

  return head


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
  result = reverse_every_k_elements(head, 3)
  print("Nodes of reversed LinkedList are: ", end='')
  result.print_list()


main()