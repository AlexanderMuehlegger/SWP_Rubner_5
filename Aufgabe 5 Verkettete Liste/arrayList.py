
class ArrayList():
    def __init__(self):
        self.array = [None] * 10

    def append(self, obj):
        def wrapper():
            for i in range(len(self)):
                if self.array[i] != None:
                    continue

                self.array[i] = obj
                return True
            return False     
        
        if wrapper() == False:
            self.array + ([None]*10)
            self.append(obj)


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
        print(charList)
        del charList[-1]
        charList[-1] = "]"

        return "".join(charList)



myArr = ArrayList()
print(myArr)
