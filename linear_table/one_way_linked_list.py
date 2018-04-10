class LinkedListUnderflow(ValueError):
    pass

class LNode:
    def __init__(self,elem,next_ = None):
        self.elem = elem
        self.next = next_

head = LNode(1)
p = head

for item in range(2,11):
    p.next = LNode(item)
    p = p.next

p = head

# while(p is not None):
#     print(p.elem)
#     p = p.next

# one way ll with a start pointer
class LList:
    def __init__(self):
        self._head = None
        self._length = 0

    @property
    def head(self):
        return self._head

    def is_empty(self):
        return self._head is None

    def prepend(self,elem):
        self._head = LNode(elem,self._head)
        self._length += 1

    def shift(self):
        if self._head is None:
            raise LinkedListUnderflow('wrong shift')
        p = self._head
        self._head = self._head.next
        self._length -= 1
        return p.elem

    def append(self,elem):
        if self._head is None:
            self._head = LNode(elem)
        else:
            p = self._head
            while p.next is not None:
                p = p.next
            p.next = LNode(elem)
        self._length += 1

    def pop(self):
        if self._head is None:
            raise LinkedListUnderflow('wrong pop')
        elif(self._length == 1):
            self._head = None
            self._length -= 1
        else:
            p = self._head
            while p.next.next is not None:
                p = p.next
            e = p.next
            p.next = None
            self._length -= 1
            return e.elem

    def find_first(self,pred):
        p = self._head
        while p is not None:
            if pred(p.elem):
                return p.elem
            p = p.next

    def filter(self,pred):
        if callable(pred):
            p = self._head
            while p is not None:
                if pred(p):
                    yield p.elem
                p = p.next

    def printall(self):
        p = self._head
        if p is None:
            return None
        else:
            while p is not None:
                print(p.elem,end='')
                if p.next is not None:
                    print(', ',end='')
                p = p.next

    def foreach(self,pred):
        if callable(pred):
            p = self._head
            while p is not None:
                pred(p.elem)
                p = p.next

    def elements(self):
        p = self._head
        while p is not None:
            yield p.elem
            p = p.next

    def insert(self,i,elem):
        if i<0 or i>self._length:
            raise LinkedListUnderflow("wrong insert , out of range")
        if i == 0:
            self.prepend(elem)
        elif i == self._length:
            self.append(elem)
        else:
            start_tag = 0
            p = self._head
            while p is not None:
                if start_tag + 1 == i:
                    p.next = LNode(elem,p.next)
                    self._length += 1
                    return
                start_tag += 1
                p = p.next


L1 = LList()

for item in range(11,21):
    L1.append(item)

for item in list(range(1,11))[::-1]:
    L1.prepend(item)
# L1.foreach(lambda x:print(x*2,end="-"))

# for i in L1.elements():
    # print(i)



# L1.prepend(7)

# L1.printall()
# L1.insert(2,998)
# print()
# L1.printall()

# add a pointer to end of list
class LList1(LList):

    def __init__(self):
        super().__init__()
        self._rear = None

    def prepend(self,elem):
        self._head = LNode(elem,self._head)
        if self._rear is None:
            self._rear = self._head

    def append(self,elem):
        if self._head is None:
            self._head = LNode(elem, self._head)
            self._rear = self._head
        else:
            self._rear.next = LNode(elem)
            self._rear = self._rear.next


    def pop(self):
        if self._head is None:
            raise LinkedListUnderflow
        p = self._head
        if p.next is None:
            self._head = None
            return p.elem
        while p.next.next is not None:
            p = p.next
        elem = p.next.elem
        p.next = None
        self._rear = p
        return elem

L2 = LList1()

for item in range(11,21):
    L2.append(item)

for item in list(range(1,11))[::-1]:
    L2.prepend(item)

L2.pop()

