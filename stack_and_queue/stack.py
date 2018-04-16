from linear_table.one_way_linked_list import LNode

class StackUnderflow(ValueError):
    pass

class SStack():
    def __init__(self):
        self._elems = []

    def is_empty(self):
        return self._elems == []

    def top(self):
        if self.is_empty():
            raise StackUnderflow('wrong top')
        return self._elems[-1]

    def push(self,elem):
        self._elems.append(elem)

    def pop(self):
        if self.is_empty():
            raise StackUnderflow('wrong pop')
        return self._elems.pop()

class LStack():
    def __init__(self):
        self._top = None

    def is_empty(self):
        return self._top is None

    def top(self):
        if self.is_empty():
            raise StackUnderflow('wrong top')
        return self._top.elem

    def push(self,elem):
        self._top = LNode(elem,next_=self._top)

    def pop(self):
        if self.is_empty():
            raise StackUnderflow('wrong top')
        p = self._top
        self._top = self._top.next
        return p.elem