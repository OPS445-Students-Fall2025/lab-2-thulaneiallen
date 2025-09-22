#!/usr/bin/env python3

# Author: Thulanei Allen
# Author ID: tallen11
# Date Created: 2025/09/21

import sys

# Check if a command line argument was provided
if len(sys.argv) > 1:
    timer = int(sys.argv[1])
else:
    timer = 3

while timer != 0:
    print(timer)
    timer -= 1

print("blast off!")