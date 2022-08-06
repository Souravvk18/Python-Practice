#  This section is common for both methods. 
class HashTable:
    def __init__(self):
        self.MAX = 100
        self.arr = [None for i in range(self.MAX)]
    def get_hash(self, key):
        h= 0
        for char in key:
            h +=ord(char)
        return h% self.MAX

#  THis section is the method one to get the input values.

    # def add(self, key , val):
    #     h = self.get_hash(key)
    #     self.arr[h]= val

    # def get(self, key):
    #     h = self.get_hash(key)
    #     return self.arr[h]

#  THis is the 2nd method to get the input values.
    def __setitem__(self, key , val):
        h = self.get_hash(key)
        self.arr[h]= val

    def __getitem__(self, key):
        h = self.get_hash(key)
        return self.arr[h]

'''
# for 1st methods--

python -i hashtable.py

>>> t= HashTable()
>>> t.add('march 6', 130)
>>> t.get('march 6')
130
t.add('march 10', 200)
>>> t.get('march 10')
200

# for 2nd methods--

python -i hashtable.py

>>> t=HashTable()
>>> t['march 10'] = 200
>>> t['march 15'] = 100
>>> t['jan 5'] = 30
>>> t['feb 14']= 50

>>> t['feb 14']
50
>>> t['march 15']
100
'''
