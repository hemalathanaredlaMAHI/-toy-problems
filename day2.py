from collections import OrderedDict

class Lru_cache:

    def __init__(self,capacity):
        self.dct=OrderedDict()
        self.capacity=capacity
        
    def get(self,key):
        if key not in self.dct:
            return -1
        else:
            a=self.dct[key]
            del self.dct[key]
            self.dct[key]=a
            return self.dct[key]
        
    def put(self,key,val):
        if len(self.dct) == self.capacity:
            self.dct.popitem(last = True)
        self.dct[key] = val
        a=self.dct[key]
        del self.dct[key]
        self.dct[key]=a
        
    def get_cache(self):
        print(self.dct)
     
a=Lru_cache(3)
a.put(1,1)
assert(a.dct)==OrderedDict([(1, 1)])
a.get_cache()
a.put(2,2)
assert(a.dct)==OrderedDict([(1, 1), (2, 2)])
a.get_cache()
a.get(1)
assert(a.dct)==OrderedDict([(2, 2), (1, 1)])
a.get_cache()
a.put(3,3)
assert(a.dct)==OrderedDict([(2, 2), (1, 1), (3,3)])
a.get_cache()
a.put(4,3)
assert(a.dct)==OrderedDict([(2, 2), (1, 1), (4, 3)])
a.get_cache()