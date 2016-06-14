from stack import Stack

def divideby2(decnumber):
    remstack = Stack()

    while decnumber > 0:
        rem = decnumber % 2
        remstack.push(rem)
        decnumber = decnumber // 2

    bin_string = ""
    while not remstack.isEmpty():
        bin_string = bin_string + str(remstack.pop())

    return bin_string

print(divideby2(42))
