#!/usr/bin/env python3

# Author: Thulanei Allen
# Author ID: tallen11
# Date Created: 2025/09/21

import sys

# Assign the first command line argument as an integer to timer
timer = int(sys.argv[1])

while timer != 0:
    print(timer)
    timer -= 1

print("blast off!")