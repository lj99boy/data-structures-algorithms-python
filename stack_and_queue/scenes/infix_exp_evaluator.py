from stack_and_queue.scenes.trans_infix_suffix import tokens,priority,infix_operators
from stack_and_queue.stack import SStack

def infix_exp_evaluator(line):
    operatorStack = SStack()
    valueStack = SStack()

    for item in tokens(line):
        #process for resolving operators
        if item in infix_operators:
            if item == '(':
                operatorStack.push(item)
            elif item == ')':
                if(operatorStack.is_empty()):
                    raise SyntaxError('wrong )')
                while operatorStack.top()!='(' and not operatorStack.is_empty():
                    right = valueStack.pop()
                    left = valueStack.pop()
                    valueStack.push(calculate(left,right,operatorStack.pop()))
                if operatorStack.is_empty():
                    raise SyntaxError('missing (')
                operatorStack.pop()
            else:
                if priority[operatorStack.top()] > priority[item]:
                    right = valueStack.pop()
                    left = valueStack.pop()
                    valueStack.push(calculate(left,right,operatorStack.pop()))
                operatorStack.push(item)
        else:
            valueStack.push(item)

    while not operatorStack.is_empty():
        right = valueStack.pop()
        left = valueStack.pop()
        valueStack.push(calculate(left,right,operatorStack.pop()))

    return valueStack.pop()





def calculate(left,right,operator):
    if operator == "+":
        res =  left+right
    elif operator == '-':
        res = left-right
    elif operator == '*':
        res = left*right
    elif operator == '/':
        res = left/right
    return res

print(infix_exp_evaluator('(3 - 5) * (6+17*4)/3'))