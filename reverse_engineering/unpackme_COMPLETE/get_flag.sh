#!/bin/bash

echo 754635 | ./unpackme-upx | grep -oE picoCTF{.*} --color=none > flag.txt
