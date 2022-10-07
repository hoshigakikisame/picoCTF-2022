#!/bin/bash

echo -ne '\n' | python3 bloat.flag.py | grep 'picoCTF{.*}' | tee flag.txt