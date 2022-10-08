#!/bin/python3

import pwn

pwn.context.log_level = 'critical'

timeout = 0.431
chrFoundCount = 0
payload = '0'*8

while True:
    p = pwn.process('./pin_checker')
    p.recv()
    p.sendline(payload)
    # print(payload)
    output = p.recvall(timeout=timeout)

    # print(output)
    payloadList = list(payload)

    if b'Access denied.' not in output:
        # print(payload)
        chrFoundCount += 1
        # print(chrFoundCount)
        timeout += 0.22
        with pwn.context.local(log_level='info'):
            pwn.log.info(f'Leaked PIN : {payload}')
    else:
        if (int(payloadList[chrFoundCount])+1) < 10:
            payloadList[chrFoundCount] = str(int(payloadList[chrFoundCount])+1)
        else:
            payloadList[chrFoundCount] = '0'

    payload = ''.join(payloadList)

    if (chrFoundCount > 7):
        break

    p.close()

open('pin', 'w').write(payload)

with pwn.context.local(log_level='info'):
    pwn.log.success(f'Found PIN : {payload}')
