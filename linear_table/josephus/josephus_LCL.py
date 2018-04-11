from linear_table.linked_cycled_list import LCList

def josephus_LCL(n,k,m):
    def turn(lcl,t):
        for i in range(t):
            lcl.rear = lcl.rear.next

    lcl = LCList()
    for item in range(1,n+1):
        lcl.append(item)

    turn(lcl,k)
    # p = lcl.rear.next
    # while k > 1:
    #     p = p.next
    #     k -= 1
    # while n>0:
    #     tm = m
    #     while tm > 1:
    #         p = p.next
    #         tm -= 1
    #     print(p.next.elem)
    #     p.next = p.next.next
    #     n -= 1
    while not lcl.is_empty():
        turn(lcl,m-1)
        print(lcl.pop())



josephus_LCL(10,3,2)

