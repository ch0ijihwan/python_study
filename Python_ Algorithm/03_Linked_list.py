#연결리스트 : 데이터와 다음 노드를 가리키는 링트를 묶어서 노드로 정의하여 사용. 
#c++이나 c에서는 포인터의 개념으로 링크를 사용하지만, 파이썬은 포인터라는 개념이 없기 때문에, 사용하지 않음

class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

def init_list():#연결리스트를 초기화 하는 기능
    global node_A
    node_A = Node("A")
    node_B = Node("B")
    node_C = Node("C")
    node_D = Node("D")

    node_A.next = node_B
    node_B.next = node_C
    node_C.next = node_D

def print_list():
    global node_A
    node = node_A
    while node:
        print(node.data)
        node = node.next
    print

if __name__ =='__main__':
    init_list()
    print_list()