#!/usr/bin/env python

import sys
import re

with open(sys.argv[1], "r", encoding="UTF-8") as file:
    buffer = {}
    index = "0000-00-00"
    tnx=0
    for line in file:
        if re.match(r'\d\d\d\d-\d\d-\d\d', line):
            index = line[:10]
            if index not in buffer:
                buffer[index] = []
                tnx=0
                buffer[index].append([line])
            else:
                tnx=len(buffer[index])
                buffer[index].append([line])
        else:
            buffer[index][tnx].append(line)
    for i in sorted(buffer.keys()):
        for j in buffer[i]:
            print("".join(j))
