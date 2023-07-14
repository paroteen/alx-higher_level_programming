#!/usr/bin/python3
"""
import sys
from collections import defaultdict

# Initialize variables
total_size = 0
status_counts = defaultdict(int)
line_count = 0

try:
    # Read input line by line from stdin
    for line in sys.stdin:
        # Split the line into different parts
        parts = line.split()

        # Extract relevant information from the line
        status_code = parts[-3]
        file_size = int(parts[-1])

        # Update total file size
        total_size += file_size

        # Update status code count
        status_counts[status_code] += 1

        # Increment line count
        line_count += 1

        # Check if 10 lines have been processed
        if line_count % 10 == 0:
            # Print statistics
            print("File size:", total_size)
            for code in sorted(status_counts.keys(), key=int):
                print(code + ":", status_counts[code])
            print()

except KeyboardInterrupt:
    # Interrupted by Ctrl+C
    print("File size:", total_size)
    for code in sorted(status_counts.keys(), key=int):
        print(code + ":", status_counts[code])
