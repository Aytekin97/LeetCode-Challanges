import math
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def add_to_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

l1 = LinkedList()
l1.add_to_beginning(1)
l1.add_to_beginning(2)
l1.add_to_beginning(3)

l2 = LinkedList()
l2.add_to_beginning(4)
l2.add_to_beginning(5)
l2.add_to_beginning(6)

def add_linked_lists (l1, l2):
    current = l1.head
    l1Extract = []
    while current:
        l1Extract.insert(0, current.data)
        current = current.next
    current = l2.head
    l2Extract = []
    while current:
        l2Extract.insert(0, current.data)
        current = current.next
    total=0
    for i in range(len(l1Extract)):
        total += (l1Extract[i] + l2Extract[i])*(10**i)
    print(total)
    create_node(total)

def create_node(num):
    l3 = LinkedList()
    listOfNum = []
    for i in range(len(str(num))):
        listOfNum.append(num%10)
        num = math.floor(num/10)
    for i in range(len(listOfNum)):
        l3.add_to_beginning(listOfNum[i])
    print(listOfNum)
    current = l3.head
    while current:
        print(current.data)
        current = current.next
        
add_linked_lists(l1, l2)