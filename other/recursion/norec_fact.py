from stack_and_queue.stack import SStack

def norec_fact(n):
    res = 1
    st = SStack()

    while n > 0:
        st.push(n)
        n -= 1

    while not st.is_empty():
        res = res*st.pop()

    return res

print(norec_fact(4))