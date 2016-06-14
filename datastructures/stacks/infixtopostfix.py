from stack import Stack

def infix_to_postfix(infixexpr):
    prec = {}
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1
    opStack = Stack()
    postfix_list = []
    token_list = infixexpr.split()

    for token in token_list:
        if token in "ABCDEFGIJKLMNOPQRSTUVWXYZ" or \
            token in "0123456789":
              postfix_list.append(token)
        elif token == "(":
            opStack.push(token)
        elif token == ")":
            topToken = opStack.pop()
            while topToken != "(":
                postfix_list.append(topToken)
                topToken = opStack.pop()
        else:
            while (not opStack.isEmpty()) and \
                (prec[opStack.peek()] >= prec[token]):
                  postfix_list.append(opStack.pop())
            opStack.push(token)

    while not opStack.isEmpty():
        postfix_list.append(opStack.pop())
    return " ".join(postfix_list)

print(infix_to_postfix("A * B + C * D"))
print(infix_to_postfix("( A + B ) * C - ( D - E ) * ( F + G )"))
