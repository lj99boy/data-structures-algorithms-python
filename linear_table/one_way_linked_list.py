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

class LList:
    def __init__(self):
        self._head = None
        self._length = 0

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

    def find(self,pred):
        p = self._head
        while p is not None:
            if pred(p.elem):
                return p.elem
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



L1 = LList()

for item in range(11,21):
    L1.append(item)

for item in list(range(1,11))[::-1]:
    L1.prepend(item)

# L1.prepend(7)

L1.printall()
