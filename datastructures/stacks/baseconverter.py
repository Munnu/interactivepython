from stack import Stack

def base_converter(dec_number, base):
    digits = '0123456789ABCDEF'

    remstack = Stack()

    while dec_number > 0:
        rem = dec_number % base
        remstack.push(rem)
        dec_number = dec_number // base

    new_string = ""
    while not remstack.isEmpty():
        new_string = new_string + digits[remstack.pop()]

    return new_string
