from linear_table.one_way_linked_list import LNode,LList1,LinkedListUnderflow

class DLNone(LNode):
    def __init__(self,elem,prev=None,next_=None):
        super().__init__(elem,next_)
        self.prev = prev


class DLList(LList1):
    def __init__(self):
        super().__init__()

    def prepend(self,elem):
        p = DLNone(elem, None, self._head)
        if self._head is None:
            self._rear = p
        else:
            p.next.prev = p
        self._head = p


    def append(self,elem):
        p = DLNone(elem, self._rear, None)
        if self._head is None:
            self._head = p
        else:
            p.prev.next = p
        self._rear = p


    def shift(self):
        if self._head is None:
            raise LinkedListUnderflow
        p = self._head
        if self._head == self._rear:
            self._head = None
            self._rear = None
        else:
            self._head = self._head.next
            self._head.prev = None
        return p.elem

    def pop(self):
        if self._head is None:
            raise LinkedListUnderflow
        p = self._rear
        if self._head == self._rear:
            self._head = None
            self._rear = None
        else:
            self._rear = p.prev
            self._rear.next = None
        return p.elem

    def reverse(self):
        self._head,self._rear = self._rear,self._head
        self._head.next,self._head.prev = self._head.prev,self._head.next
        p = self._head
        while p.next is not None:
            p.next.next,p.next.prev = p.next.prev,p.next.next
            p = p.next







L1 = DLList()

for item in range(11,21):
    L1.append(item)
    pass

for item in list(range(1,11))[::-1]:
    # L1.prepend(item)
    pass
# L1.pop()
L1.reverse()

L1.printall()