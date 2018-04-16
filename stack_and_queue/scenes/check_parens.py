from stack_and_queue.stack import SStack

def check_parens(text):
    parens = "(){}[]"
    open_parens = "({["
    opposite = {")": "(", "{": "}", "[": "]"}

    def parentheses(text):
        """ yield parents in text """
        i,text_len = 0,len(text)
        while True:
            if i<text_len and text[i] not in parens:
                i = i+1
            if i>=text_len:
                return
            yield text[i],i
            i += 1

    st = SStack()

    for pr,index in parentheses(text):
        if pr in open_parens:
            st.push(pr)
        elif st.pop()!= opposite[pr]:
            print("Unmatching is found at", index,"for",pr)
            return False

    print("All parentheses are correctly matched")
    return True

