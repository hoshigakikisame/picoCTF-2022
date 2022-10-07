import string

uppercase = string.ascii_uppercase
decimals = string.digits

flag = []

with open('message.txt') as filp:
    rawMessage = filp.read()
    strings = rawMessage.split()
    integers = [int(val) for val in strings]

    for integer in integers:
        modded = integer % 37

        if modded in range(0, 26):
            flag.append(uppercase[modded])
        elif modded in range(26, 36):
            flag.append(decimals[modded - 26])
        else:
            flag.append('_')

    print(f"picoCTF{{{''.join(flag)}}}")
