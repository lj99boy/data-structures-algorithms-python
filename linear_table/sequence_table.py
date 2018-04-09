"""
 a sequence-table base on python-list


"""

class SequenceTableValueError(ValueError):
    pass


class SequenceTable:

    def __init__(self):
        self._max_length = 3
        self._num = 0
        self._store = []

    @property
    def store(self):
        return self._store

    @property
    def num(self):
        return self._num

    @property
    def max_length(self):
        return self._max_length

    def is_empty(self):
        if self._num == 0:
            return True

    def len(self):
        return self._num

    def extend_store(self):
        self._max_length = self._max_length * 2
        new_store = []
        index = 0
        for i in self._store:
            new_store.insert(index,i)
            index += 1
        self._store = new_store

    def prepend(self,elem):
        if self._num == self._max_length:
            self.extend_store()
        end_tag = self._num
        if(end_tag == 0):
            self._store.insert(0,elem)
        else:
            for item in self._store[::-1]:
                if (end_tag == self._num):
                    self._store.insert(end_tag, item)
                else:
                    self._store[end_tag] = item
                end_tag -= 1
            self._store[0] = elem
        self._num += 1

    def append(self,elem):
        if self._num == self._max_length:
            self.extend_store()
        self._store.insert(self._num,elem)
        self._num += 1

    def insert(self,elem,i):
        if self._num == self._max_length:
            self.extend_store()

        if(i<0 or i>self._num):
            raise SequenceTableValueError('out of range')
        elif(i==0):
            self.prepend(elem)
        elif(i==self._num):
            self.append(elem)
        else:
            end_tag = self._num
            for item in self._store[:i-1:-1]:
                if(end_tag == self._num):
                    self._store.insert(end_tag,item)
                else:
                    self._store[end_tag] = item
                end_tag -=1
            self._store[i] = elem
            self._num += 1

    def del_first(self):
        start_tag = 0
        for item in self._store[1:]:
            self._store[start_tag] = item
            start_tag += 1
        del self._store[self._num-1]
        self._num -= 1

    def del_last(self):
        del self._store[self._num-1]
        self._num -= 1

    def del_item(self,i):
        if(i<0 or i>self._num-1):
            raise SequenceTableValueError('out of range')
        elif(i == 0):
            self.del_first()
        elif(i == self._num-1):
            self.del_last()
        else:
            start_tag = i
            for item in self._store[i+1:]:
                self._store[start_tag] = item
                start_tag += 1
            del self._store[self._num-1]
            self._num -= 1


    def search(self):
        pass

    def __str__(self):
        return ",".join(str(self._store))

    

s1 = SequenceTable()
print(s1.num)
print(s1.max_length)


s1.prepend(1)
s1.prepend(2)
s1.prepend(3)
s1.prepend(4)
s1.append(9)
# s1.append(2)
# s1.append(3)
# s1.append(4)
s1.insert(7,1)
s1.del_item(4)
# s1.del_first()
# s1.del_last()
# s1.insert(7,1)
# print(s1.store[:2:-1])

print(s1.store)
print(s1.num)
print(s1.max_length)