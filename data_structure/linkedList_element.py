class LinkedListElement : #노드
    def __init__(self, val, ptr) :
        self.value = val
        self.myNext = ptr

node1 = LinkedListElement(10, None)
node2 = LinkedListElement(20, None)
node3 = LinkedListElement(30, None)

# print(node1.value)
node1.myNext = node2 #myNext 필드에 node2를 넣어줌
node2.myNext = node3

print(node1.value)
print(node1.myNext.value)
print(node1.myNext.myNext)
print(node1.myNext.myNext.value)