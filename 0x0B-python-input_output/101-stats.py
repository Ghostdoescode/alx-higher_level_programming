#!/usr/bin/python3
"""Reads from standard input and computes metrics
"""

import sys
import signal

total_size = 0
status_codes = {}
line_count = 0

def handle_interrupt(signal, frame):
    print_stats()
    sys.exit(0)

signal.signal(signal.SIGINT, handle_interrupt)

def print_stats():
    global total_size, status_codes, line_count
    print("Total file size: ", total_size)
    for code in sorted(status_codes.keys()):
        print(f"{code}: {status_codes[code]}")
    print("Line count: ",line_count)
    total_size = 0
    status_codes = {}
    line_count = 0

for line in sys.stdin:
    fields = line.strip().split(" ")
    if len(fields) != 6:
        continue

    ip, date, request, status_code, status_text, size = fields
    total_size += int(size)
    line_count +=1
    if status_code in status_codes:
        status_codes[status_code] += 1
    else:
        status_codes[status_code] = 1

    if line_count % 10 == 0:
        print_stats()
