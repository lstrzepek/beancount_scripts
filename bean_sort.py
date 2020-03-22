#!/usr/bin/env python

import sys
import re

with open(sys.argv[1], "r", encoding="UTF-8") as file:
    buffer = {}
    index = "0000-00-00"
    for line in file:
        if re.match(r'\d\d\d\d-\d\d-\d\d', line):
            index = line[:10]
            buffer[index] = []
        buffer[index].append(line)
    for i in sorted(buffer.keys()):
        print("".join(buffer[i]))
