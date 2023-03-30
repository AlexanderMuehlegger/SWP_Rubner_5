from MyList import VerketteteListe, Node

class DopNode(Node):
    def __init__(self, obj):
        super(DopNode, self).__init__(obj)
        self.last = None
    
    def getLast(self):
        return self.last
    
    def setLast(self, node):
        self.last = node
        

class DoppeltVerketteteListe(VerketteteListe):
    def __init__(self):
        super(DoppeltVerketteteListe, self).__init__()
        self.startNode = DopNode('Head')
        self.lastNode = DopNode('Tale')

    def add(self, obj):
        newNode = DopNode(obj)
        newNode.setNext(self.lastNode)
        self.lastNode.setLast(newNode)

    def getLastNode(self):
        return self.lastNode
