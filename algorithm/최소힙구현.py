class PriorityQueue:
    '''
    우선순위 큐를 힙으로 구현합니다
    '''

    def __init__(self) :
        self.data = [0]

    def push(self, value) :
        '''
        우선순위 큐에 value를 삽입합니다.
        '''
        self.data.append(value)

        #만약 해당 값이 부모노드보다 크면 멈추기, 작으면 순서 바꾸기
        #부모노드는 자식노드인덱스 // 2
        for i in range(len(self.data)):
            if len(self.data) < 2:
                pass
            elif self.data[i] >= self.data[i//2]:
                pass
            elif self.data[i] < self.data[i//2]:
                parent = self.data[i//2]
                child = self.data[i]
                self.data[i//2] = child
                self.data[i] = parent
            
            
        
    def pop(self) :
        '''
        우선순위가 가장 높은 원소를 제거합니다.
        '''

        del self.data[1]
        

    def top(self) :
        '''
        우선순위가 가장 높은 원소를 반환합니다. 만약 우선순위 큐가 비어있다면 -1을 반환합니다.
        '''
        if len(self.data) == 1:
            return -1
        else:     
            return self.data[1]
queue = PriorityQueue()
queue.push(1)
queue.push(4)
queue.push(3)
queue.push(2)
print(queue.top())
queue.pop()
print(queue.top())
queue.pop()
print(queue.data)