from linear_table.one_way_linked_list import LList

# insert sort using in sequence list
def list_sort(lst):
    for i in range(1,len(lst)):
        x = lst[i]
        j = i
        while j > 0 and lst[j-1]>x:
            lst[j] = lst[j-1]
            j -= 1
        lst[j] = x

# insert sort using in one way ll
def one_way_sort(lst):
    if lst.head is None:
        return
    crt = lst.head.next
    while crt is not None:
        p = lst.head
        x = crt.elem
        while p is not crt and p.elem <= x :
            p = p.next
        while p is not crt:
            y = p.elem
            p.elem = x
            x = y
            p = p.next
        crt.elem = x
        crt = crt.next

l1 = LList()
l1.append(3)
l1.append(2)
l1.append(4)
l1.append(1)

l1.printall()
one_way_sort(l1)
l1.printall()
