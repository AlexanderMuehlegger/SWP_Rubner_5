def add_element(func):
    def wrapper(*args, **kwargs):
        new_node = func(*args, **kwargs)
        last_node = args[0].getLastNode()
        last_node.setNext(new_node)
        return f"Added '{args[1]}' to the list"
    return wrapper

def last_element(func):
    def wrapper(*args, **kwargs):
        last_node = func(*args, **kwargs)
        while(last_node.getNext() != None):
            last_node = last_node.getNext()
        return last_node
    return wrapper

def delete_element(func):
    def wrapper(*args, **kwargs):
        start_el = func(*args, **kwargs)
        deleted = False
        while(start_el.getNext() != None and start_el.getObj() is not args[1]):
            if start_el.getNext().getObj() is args[1]:
                if start_el.getNext().getNext() is not None:
                    start_el.setNext(start_el.getNext().getNext())
                else:
                    start_el.setNext(None)
                    break
                deleted = True
            start_el = start_el.getNext()
        return f"Deleted '{args[1]}' from List" if deleted else f"'{args[1]}' does not exist"
    return wrapper

def print_list(func):
    def wrapper(*args, **kwargs):
        start_el = func(*args, **kwargs)
        toReturn = []
        while(start_el.getNext() != None):
            if start_el.getObj() != 'Head':
                toReturn.append(start_el.getObj())
            start_el = start_el.getNext()
        if(start_el.getObj() != 'Head'):
            toReturn.append(start_el.getObj())
        return str(toReturn)
        
    return wrapper

def insert_element(func):
    def wrapper(*args, **kwargs):
        pointer, new_node = func(*args, **kwargs)
        while(pointer.getNext() != None and pointer.getObj() is not args[1]):
            pointer = pointer.getNext()

        next_node = pointer.getNext()
        pointer.setNext(new_node)
        new_node.setNext(next_node)
        return f'Inserted {args[2]} after {args[1]}'
    return wrapper

def find_element(mode):
    def find_element_dec(func):
        def wrapper(*args, **kwargs):
            node = func(*args, **kwargs)
            index = 0
            if(mode=='GetObj' and args[1] > args[0].length):
                return IndexError("Out of Bounds")
            while(node.getNext() != None or node.getNext() == None and mode == 'GetObj'):
                if(node.getObj() == 'Head'):
                    node = node.getNext()
                    continue
                if(mode == 'GetObj'):
                    if(args[1] == index):
                        return node.getObj()
                if(node.getObj() is args[1]):
                    return True if (mode == 'NoIndex') else index
                node = node.getNext()
                index += 1
            return False if (mode == 'NoIndex') else index if (mode != 'GetObj') else 'Couldnt find Object'
        return wrapper
    return find_element_dec

def clear(func):
    def wrapper(*args, **kwargs):
        args[0].length = 0
        args[0].startNode.setNext(None)
    return wrapper 


