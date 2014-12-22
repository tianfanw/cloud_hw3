#!/usr/bin/env python

import sys

keyword = "school"

# input comes from STDIN (standard input)
for line in sys.stdin:

    line = line.strip()
    # split the line into words
    words = line.split()
    # increase counters

    isRelated = False
    for word in words:
        if word == keyword:
            isRelated = True
            break
    if isRelated:
        for word in words:
            if word != keyword:
                print '%s\t%s' % (word, 1)