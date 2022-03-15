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


def reverse_sub_list(head, p, q):
  previous = None
  current = head
  i = 1
  while current:
    if i >= p and i <= q:
      next = current.next
      current.next = previous
      previous = current
      current = next
    elif i < p:
      before = current
      current = current.next
    else:
        break
    
    i+= 1

  if i == q+1:
    before.next.next = current
    before.next = previous

  return head



def main():
  head = Node(1)
  head.next = Node(2)
  head.next.next = Node(3)
  head.next.next.next = Node(4)
  head.next.next.next.next = Node(5)

  print("Nodes of original LinkedList are: ", end='')
  head.print_list()
  result = reverse_sub_list(head, 2, 4)
  print("Nodes of reversed LinkedList are: ", end='')
  result.print_list()


main()
