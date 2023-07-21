#!/usr/bin/python3

import re
import sys

# Constants
STATUS_CODES = {200, 301, 400, 401, 403, 404, 405, 500}

# Initialize variables
total_size = 0
status_code_counts = {status_code: 0 for status_code in STATUS_CODES}

# Read lines from stdin
for line in sys.stdin:
    # Parse the line
    match = re.match(r"^(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - \[(.*)\] \"GET /projects/260 HTTP/1.1\" (\d+) (\d+)$", line)
    if match:
        # Update the total file size
        total_size += int(match.group(5))

        # Update the status code counts
        status_code = int(match.group(4))
        status_code_counts[status_code] += 1

    # Print the metrics every 10 lines
    if len(status_code_counts) % 10 == 0:
        print("File size:", total_size)
        for status_code, count in status_code_counts.items():
            print(status_code, ":", count)
