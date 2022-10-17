#!usr/bin/env python3

# Tool to assist in reviewing server logs.
# Useful in creating samples for reporting, or just counting occurrences.
# Searches log files for lines containing a given IP (or any other string)
# and appends each line found to a txt file with the string as filename.
#
# To Use:
#   1. Run script: python scanner.py auth.log "Invalid user"
#   2. Script will create ./results/outputFile containing all matching lines

import argparse
import os
from datetime import datetime

parser = argparse.ArgumentParser(description='Log scanner')
parser.add_argument('logfile', help='Log file to scan')
parser.add_argument('searchquery', help='IP or string to search for')
parser.add_argument('-printresults', help='Print results to terminal', action='store_true')
args = parser.parse_args()

inputFile = args.logfile
ip = args.searchquery

dataLog = [] # for future use

# Using timestamp for output filename, to avoid appending to an existing file.
# Also I want the timestamps to sort lexicographically
now = datetime.now()
timestamp = now.strftime('%m.%d-%H.%M') # format timestamp as MM.DD-HH.MM ex. 10.03-20.40
outputFile = f'./results/{ip}--{timestamp}.txt'

# read the log file
with open(inputFile, 'rt') as f:
    data = f.readlines()

# create the output directory if it doesn't exist
os.makedirs(os.path.dirname(outputFile), exist_ok=True)

def searchFor(searchQuery):
    for line in data:
        if line.__contains__(searchQuery):
            if args.printresults:   # if using -printresults arg
                print(line)
            dataLog.append(line)
            with open(outputFile, 'a') as newFile:
                newFile.write(line)
    return dataLog

searchFor(ip)
print(f'{ip} found {len(dataLog)} times')

