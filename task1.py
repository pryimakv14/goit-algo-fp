class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self) -> str:
        elem = self
        lst = []
        while elem:
            lst.append(str(elem.data))
            elem = elem.next

        return ' -> '.join(lst)


def reverse(n: Node):
    curr = n.next
    prev = n
    n.next = None
    while curr:
        nxt_node = curr.next
        curr.next = prev

        prev = curr
        curr = nxt_node

    return prev


def sort(node: Node):
    if(node is None):
        return
    temp=node
    while temp != None:
        i=temp.next
        while i != None:
            if temp.data > i.data:
                n = i.data
                i.data = temp.data
                temp.data = n
            i = i.next
        
        temp = temp.next

    return node


def merge_sorted(n1: Node, n2: Node):
    first = n1
    last = n1
    while last.next:
        last = last.next

    last.next = n2

    return sort(first)


if __name__ == "__main__":
    n1 = Node(1)
    n2 = Node(3)
    n3 = Node(5)
    n4 = Node(8)
    n5 = Node(10)
    n6 = Node(12)

    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5
    n5.next = n6

    nn1 = Node(9)
    nn2 = Node(11)
    nn3 = Node(6)
    nn4 = Node(14)
    nn5 = Node(7)
    nn6 = Node(4)

    nn1.next = nn2
    nn2.next = nn3
    nn3.next = nn4
    nn4.next = nn5
    nn5.next = nn6

    print("Reverse: ", reverse(n1))
    print("Sort: ", sort(nn1))

    # n6 bc it's already reversed
    print("Merge and sort: ", merge_sorted(n6, nn1))
  
