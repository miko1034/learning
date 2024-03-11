BLANK = object()

class Hashtable:
    def __init__(self,size):
        self.values = size * [BLANK]
        
    def __len__(self):
        return len(self.values)
    
    def __setitem__(self,key,value):
        index = hash(key) % len(self)
        self.values[index] = value