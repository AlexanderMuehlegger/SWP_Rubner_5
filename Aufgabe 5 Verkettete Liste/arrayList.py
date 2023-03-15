
class ArrayList():
    def __init__(self):
        self.array = [None] * 10

    def append(self, obj):
        def wrapper():

            if len(self) == 0:
                self.array[0] = obj
                return

            for i in range(0, len(self)+1, 1):
                try:
                    if self.array[i] == None:
                        self.array[i] = obj
                        return True
                except IndexError:
                    pass
            return False     
        result = wrapper()
        if result == False:
            self.array = self.array + ([None]*10)
            self.append(obj)
        else:
            return
    
    def __len__(self):
        length = 0
        for i in self.array:
            if i == None:
                break
            else:
                length += 1
        return length

    def __str__(self) -> str:
        toReturn = "["
        for i in self.array:
            if i != None: toReturn += (str(i) + ", ")
        
        if toReturn == "[":
            return toReturn + "]"

        charList = list(toReturn)
        
        del charList[-1]
        charList[-1] = "]"

        return "".join(charList)



myArr = ArrayList()
print(myArr)

for i in range(20):
    myArr.append(f"item {i}")

print(myArr)
