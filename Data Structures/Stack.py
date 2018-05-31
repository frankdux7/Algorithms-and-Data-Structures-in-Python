class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

    def __repr__(self):
        return repr(self.data)

class Stack:
    def __init__(self):
        self.top = None

    def __repr__(self):
        nodes = []
        curr = self.top
        while curr:
            nodes.append(repr(curr))
            curr = curr.next
        return ','.join(nodes)



    def append(self, data):
        if not self.top:
            self.top = Node(data)
        else:
            curr = self.top
            self.top = Node(data)
            self.top.next = curr

    def pop(self):
        curr = self.top
        new_next = curr.next
        self.top = curr.next
        self.top.next = new_next.next
        return curr



words = Stack()
words.append('boby')
words.append('pesho')
words.append('koko')
words.append('ivo')
print(words)
print('Pop first element....')
print(words.pop())
print(words)
print('Pop second element...')
print(words.pop())
print(words)
