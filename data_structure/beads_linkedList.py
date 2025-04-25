'''
1. LinkedListPipe 클래스를 완성하세요.
2. procesBeads 함수를 완성하세요.
'''

class LinkedListElement :
    def __init__(self, val, ptr) :
        self.value = val
        self.myNext = ptr

class LinkedListPipe:
    '''
    Linked List를 이용하여 다음의 method들을 작성하세요.
    '''
    def __init__(self) :
        '''
        리스트 myPipe를 만듭니다. 이는 구슬의 배치를 저장합니다.
        '''
        self.start = None #연결리스트 시작점
        self.end = None #연결리스트 끝점

    def addLeft(self, n) :
        '''
        파이프의 왼쪽으로 구슬 n을 삽입합니다.
        '''
        #맨 처음(리스트에 시작 끝이 없을때)
        if self.start is None and self.end is None:
            element = LinkedListElement(n, None)
            self.start = element
            self.end = element
        else: # 시작 노드, 끝 노드가 있을 때
            element = LinkedListElement(n, self.start) #노드 하나 만들기, 노드 다음을 원래 있던 첫 노드에 연결
            self.start = element #리스트 파이프의 첫 시작을 만든 노드

    def addRight(self, n) :
        '''
        파이프의 오른쪽으로 구슬 n을 삽입합니다.
        '''
        if self.start is None and self.end is None:
            element = LinkedListElement(n, None)
            self.start = element
            self.end = element
        else:
            element = LinkedListElement(n, None)
            self.end.myNext = element # 새로 가리키는 next노드가 element임
            self.end = element #헷갈!!!!!

    def getBeads(self) :
        '''
        파이프의 배치를 list로 반환합니다.
        '''
        beads = []
        current = self.start
        #while current is not None and current != self.end
        while self.start is not None and current != self.end: #이게 핵심. 언제 시작하고 종료할지
            beads.append(current.value) #첫번째 노드부터 저장
            current = current.myNext #다음 노드 바라보도록(하나씩 이동한다. next로끝까지 이동하여 마지막까지 갈 때 멈춤)
        beads.append(current.value)
        return beads



def processBeads(myInput) :
    '''
    구슬을 파이프에 넣는 행위가 myInput으로 주어질 때, 구슬의 최종 배치를 리스트로 반환하는 함수를 작성하세요.

    myInput[i][0] : i번째에 넣는 구슬의 번호
    myInput[i][1] : i번째에 넣는 방향

    예를 들어, 예제의 경우 

    myInput[0][0] = 1, myInput[0][1] = 0,
    myInput[1][0] = 2, myInput[1][1] = 1,
    myInput[2][0] = 3, myInput[2][1] = 0

    입니다.

    '''

    myPipe = LinkedListPipe()

    result = []

    return result