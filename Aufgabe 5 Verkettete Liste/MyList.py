import random
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
    
    def setStartNode(self, node):
        self.startNode = node

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
    def __str__(self):
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

    def shuffle(self):
        indexes = list(range(self.length))
        random.shuffle(indexes)
        new_list = VerketteteListe()
        for i in indexes:
            new_list.add(self[i])
        return new_list
    
    def remove(self, value):
        prev_node = self.startNode
        now_node = self.startNode
        while(now_node != None):
            if(now_node.getObj() == value):
                prev_node.setNext(now_node.getNext())
                now_node = now_node.getNext()
                continue
            else:
                prev_node = now_node
                now_node = now_node.getNext()

    def middle(self, head):
        if(head == None):
            return None
        
        slow = head
        fast = head

        while(fast.getNext() != None and fast.getNext().getNext() != None):
            slow = slow.getNext()
            fast = fast.getNext().getNext()

        return slow

    @find_element(mode='GetObj')
    def __getitem__(self, index):
        return self.startNode


    def __len__(self):
        return self.length


