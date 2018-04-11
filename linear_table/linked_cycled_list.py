from linear_table.one_way_linked_list import LNode,LinkedListUnderflow

class LCList:
    def __init__(self):
        self._rear = None

    def is_empty(self):
        return self._rear is None

    def prepend(self,elem):
        p = LNode(elem)
        if self._rear is None:
            self._rear = p
            self._rear.next = self._rear
        else:
            p.next = self._rear.next
            self._rear.next = p

    @property
    def rear(self):
        return self._rear

    @rear.setter
    def rear(self,rear):
        self._rear = rear


    def append(self,elem):
        self.prepend(elem)
        self._rear = self._rear.next

    def pop(self):
        if self._rear is None:
            raise LinkedListUnderflow
        p = self._rear.next
        if p == self._rear:
            self._rear = None
        else:
            self._rear.next = p.next
        return p.elem

    def printall(self):
        p = self._rear.next
        while p is not None:
            print(p.elem,end=' , ')
            if p == self._rear:
                return
            p = p.next

# lcl = LCList()
#
# lcl.append(1)
# lcl.append(2)
# lcl.append(3)
# lcl.append(4)
#
# lcl.printall()