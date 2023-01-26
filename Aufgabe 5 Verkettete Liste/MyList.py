class Node:
    obj = None
    next = None

    def __init__(self, obj):
        self.obj = obj
        self.next = None

    def getObj(self):
        return self.obj
    
    def getNext(self):
        return self.next
    
    def setNext(self, next):
        self.next = next
    
class VerketteteListe():
    from MyDecorators import add_element, delete_element, last_element, print_list, insert_element, find_element, clear

    def __init__(self):
        self.startNode = Node('Head')
        self.length = 0

    @add_element
    def add(self, obj):
        self.length += 1
        return Node(obj)

    @delete_element
    def delete(self, obj):
        self.length -= 1
        return self.startNode
    
    @last_element
    def getLastNode(self):
        return self.startNode
    
    @print_list
    def printList(self):
        return self.startNode

    @insert_element
    def insert(self, after, obj):
        self.length += 1
        return self.startNode, Node(obj)
    
    @find_element(mode='NoIndex')
    def contains(self, obj):
        return self.startNode
    
    @find_element(mode='Index')
    def indexOf(self, obj):
        return self.startNode
    
    @clear
    def clear(self):
        return self.startNode

    @find_element(mode='GetObj')
    def getObjByIndex(self, index):
        return self.startNode


    def getLength(self):
        return self.length


