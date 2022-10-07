import string

uppercase = string.ascii_uppercase
decimals = string.digits

flag = []

with open('message.txt') as filp:
    rawMessage = filp.read()
    strings = rawMessage.split()
    integers = [int(val) for val in strings]

    for integer in integers:
        modded = pow(integer, -1, 41)

        if modded in range(1, 27):
            flag.append(uppercase[modded - 1])
        elif modded in range(27, 37):
            flag.append(decimals[modded - 27])
        else:
            flag.append('_')

    print(f"picoCTF{{{''.join(flag)}}}")
