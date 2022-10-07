#!/bin/python3

import re

with open('KeygenMe.java') as filp:
    content = filp.read()
    pattern = re.findall(r"'.*'", content)
    rawFlag = [char for char in pattern]
    flag = "".join(rawFlag).replace("'", "")[::-1]
    filp = open("flag.txt", "w")
    filp.write(flag)
    filp.close()
