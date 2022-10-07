#!/bin/python3

# import io
# from typing import Any
import string


def decryption(cipher, masterKey):
    orig_text = []
    key = key = masterKey * int(len(cipher) / len(masterKey)) + \
        masterKey[:len(cipher) % len(masterKey)]
    for i in range(len(cipher)):
        x = (ord(cipher[i]) - ord(key[i]) + 26) % 26
        x += ord('A')
        orig_text.append(chr(x))
    return ("" . join(orig_text))


with open('cipher.txt') as filp:
    key = 'CYLAB'
    encryptedMessage = filp.read()
    flag = decryption(encryptedMessage, key)
    print(flag)
