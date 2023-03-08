from MyList import VerketteteListe, Node

class DopNode(Node):
    def __init__(self, obj, last):
        super(obj)
        self.last = last
    
    def getLast(self):
        return self.last
        

class DoppeltVerketteteListe(VerketteteListe):
    def __init__(self):
        super()
        self.lastNode = Node('Head')

    def add(self, obj):
        self.length += 1
        newNode = DopNode(obj, self.lastNode)
        self.lastNode.setNext(newNode) 

    def getLastNode(self):
        return self.lastNode
    