#!/bin/bash

echo 549255 | ./bbbbloat | grep -oE picoCTF{.*} --color=none > flag.txt
