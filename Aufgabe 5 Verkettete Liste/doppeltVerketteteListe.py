from MyList import VerketteteListe, Node

class DopNode(Node):
    def __init__(self, obj):
        super(DopNode, self).__init__(obj)
        self.last = None
    
    def getLast(self):
        return self.last
        

class DoppeltVerketteteListe(VerketteteListe):
    def __init__(self):
        super(DoppeltVerketteteListe, self).__init__()
        self.startNode = DopNode('Head')

    def add(self, obj):
        newNode = DopNode(obj)
        
        last_node = self.startNode
        while last_node.next != None:
            last_node = last_node.next
        
        newNode.last = last_node

        last_node.next = newNode

    def getLastNode(self):
        return self.lastNode
