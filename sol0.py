#!/usr/bin/env python3

import sys

buffer_size = 7

input_string = "lmsteph" + "A" * (buffer_size - len("uniqname"))

print(input_string, end='')