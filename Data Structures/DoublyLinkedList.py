class Node:
    def __init__(self, data, next = None, prev = None):
        self.data = data
        self.next = next
        self.prev = prev

    def __repr__(self):
        return repr(self.data)

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None


    def __repr__(self):
        nodes = []
        curr = self.head
        while curr:
            nodes.append(repr(curr))
            curr = curr.next
        return ','.join(nodes)

    def append(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            self.tail = self.head
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def delete(self, data):
        if self.head.data == data:
            self.head = self.head.next
        elif self.tail.data == data:
            self.tail = self.tail.prev
            self.tail.next = None
        else:
            curr = self.head
            while curr:
                if curr.data == data:
                    temp = curr
                    curr = temp.prev
                    curr.next = temp.next
                prev = curr
                curr = curr.next

    def find(self, data):
        curr = self.head
        while curr:
            if curr.data ==data:
                return curr
            curr = curr.next
        raise LookupError('Name {} not found'.format(data))

words = DoublyLinkedList()
words.append('boby')
words.append('pesho')
words.append('ivan')
words.append('gosho')
words.append('tosho')
print(words)
print('Deleting Ivan...')
words.delete('ivan')
print(words)
print('Finding gosho')
print(words.find('gosho'))
print(words.find('Koko'))
