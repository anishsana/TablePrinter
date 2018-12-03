#!/usr/local/bin/python3

# Print Table - prints tables in a formatted manner

import sys

tableData = sys.argv

for i in range(len(tableData)):
    if i != 0:
        print(tableData[i] + "\t", end="")
        if i % 3 == 0:
            print("\n")

print()
