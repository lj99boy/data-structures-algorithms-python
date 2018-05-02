class PrioQueueError(ValueError):
    pass

class PrioQue:
    def __init__(self,elist=[]):
        self.__elems = list(elist)
        self.__elems.sort(reverse=True)

    def enqueue(self,e):
        i = len(self.__elems) -1
        while i >= 0:
            if self.__elems[i]<= e:
                i -= 1
            else:
                break
        self.__elems.insert(i+1,e)

    def is_empty(self):
        return not self.__elems

    def peek(self):
        if self.is_empty():
            raise PrioQueueError('in peek')
        return self.__elems[-1]

    def dequeue(self):
        if self.is_empty():
            raise PrioQueueError("in pop")
        return self.__elems.pop()
