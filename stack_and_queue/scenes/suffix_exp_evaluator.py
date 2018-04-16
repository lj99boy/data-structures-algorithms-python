from stack_and_queue.stack import SStack

class ESStack(SStack):

    @property
    def depth(self):
        return len(self._elems)


def suffix_exp_evaluator(line):
    exp = line.split()
    operators = "+-*/"
    st = ESStack()
    for x in exp:
       if x not in operators:
            st.push(float(x))
            continue

       if st.depth < 2:
           raise SyntaxError("short of operand(s)")

       a = st.pop()
       b = st.pop()

       if x == "+":
           c = b+a
       elif x == '-':
           c = b-a
       elif x == '*':
           c = b*a
       elif x == '/':
           c = b/a

       st.push(c)

    if st.depth == 1:
        return st.pop()
    raise SyntaxError("Extra operand(s)")


print(suffix_exp_evaluator('9 3 1 - 3 * + 10 2 / +'))
