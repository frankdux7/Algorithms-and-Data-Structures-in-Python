class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

    def __repr__(self):
        return repr(self.data)


class LinkedList:
    def __init__(self):
        self.head = None

    def __repr__(self):
        nodes = []
        curr = self.head
        while curr:
            nodes.append(repr(curr))
            curr = curr.next
        return '[' + ', '.join(nodes) + ']'

    def append(self, data):
        if not self.head:
            self.head = Node(data)
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = Node(data)

    def find(self, data):
        curr = self.head
        while curr:
            if curr.data == data:
                return curr
        raise LookupError('Not found')

    def prepend(self, data):
        curr = self.head
        next_node = curr
        self.head = Node(data)
        self.head.next = next_node

    def remove(self, data):
        curr = self.head
        prev = None
        while curr:
            if curr.data == data:
                if self.head.data == data:
                    self.head = curr.next
                else:
                    temp = curr.next
                    curr = prev
                    curr.next = temp
            prev = curr
            curr = curr.next

words = LinkedList()
words.append('boby')
words.append('ivan')
words.append('gosho')
print(words)
print('Removing Boby...')
words.remove('boby')
print(words)
print('Removing Gosho...')
words.remove('gosho')
print(words)
print('Prepend Pesho...')
words.prepend('pesho')
print(words)
