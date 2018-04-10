from .one_way_linked_list import LNode,LinkedListUnderflow

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