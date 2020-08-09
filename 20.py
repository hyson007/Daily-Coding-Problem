class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data

class Linklist:
    def __init__(self):
        self.head = None
        self.next = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        last_node = self.head
        while last_node.next:
            last_node = last_node.next

        last_node.next = new_node

    def pprint(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next

    def match(self, other):
        cur_node_1 = self.head
        cur_node_2 = other.head
        while cur_node_1.data != cur_node_2.data:
            cur_node_1 = cur_node_1.next
            cur_node_2 = cur_node_2.next
        return cur_node_1.data



# n = Node(3)
L = Linklist()
L.append(3)
L.append(7)
L.append(8)
L.append(10)
# print(L.head)
L.pprint()

print('*******************')

S = Linklist()
S.append(99)
S.append(1)
S.append(8)
S.append(10)
S.pprint()

print('*******************')

print(L.match(S))
