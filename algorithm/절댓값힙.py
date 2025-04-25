class Tree:
    def __init__(self, i, l, r) :
        self.index = i
        self.left = l
        self.right = r

    def addNode(self, i, l, r) :
        '''
        트리 내의 정점 i에 대하여 왼쪽자식을 l, 오른쪽 자식을 r로
        설정해주는 함수를 작성하세요.
        '''
        self.index = i                
        self.left = l
        self.rignt = r 
        

        return


tree = Tree(1,2,3)
tree.addNode(1,2,3) 