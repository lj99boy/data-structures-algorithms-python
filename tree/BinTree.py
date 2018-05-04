class BinTNode:
    def __init__(self,dat, left = None , right=None):
        self.data = dat
        self.left = left
        self.right = right

def count_BinTNodes(t):
    if t is None:
        return 0
    else:
        return 1+count_BinTNodes(t.left)+count_BinTNodes(t.right)

def sum_BinTNodes(t):
    if t is None:
        return 0
    else:
        return t.dat +sum_BinTNodes(t.left) + sum_BinTNodes(t.right)

#root first
def preorder(t,proc):
    if t is None:
        return
    proc(t.data)
    preorder(t.left)
    preorder(t.right)

#root center
def center_preorder(t,proc):
    if t is None:
        return
    center_preorder(t.left)
    proc(t.data)
    center_preorder(t.right)

#root last
def last_preorder(t,proc):
    if t is None:
        return
    last_preorder(t.left)
    last_preorder(t.right)
    proc(t.data)


def print_BinTNodes(t):
    if t is None:
        print("^",end="")
        return
    print("("+str(t.data),end="")
    print_BinTNodes(t.left)
    print_BinTNodes(t.right)
    print(")",end="")