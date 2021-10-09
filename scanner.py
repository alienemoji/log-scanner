#!usr/bin/env python3

# Tool to assist in manually reviewing server logs.
# Useful in creating samples for reporting, or just counting occurrences.
# Searches log files for lines containing a given IP (or any other string)
# and appends each line found to a new file with the IP/string as name.
#
# To Use:
#   1. Set inputFile value with path to log file
#   2. Run script
#   3. Enter the IP/string you want to find
#   4. Script will create ./log-scanner-findings/outputFile containing all matching lines
#   5. 

import os
from datetime import datetime



inputFile = './auth.log' # replace with the log file you're scanning
# Uncomment the following line to use user input for inputFile
#inputFile = input('Log file: ')

ip = input('IP or string to search for: ') # user enters the IP/string to search for

dataLog = [] # for future use
# Using timestamp for output filename, to avoid appending to an existing file.
# Also I want the timestamps to sort lexicographically
now = datetime.now()
timestamp = now.strftime('%m.%d.%H.%M') # format timestamp as MM.DD.HH.MM ex. 10.03.20.40
outputFile = f'./log-scanner-findings/{ip}--{timestamp}.txt'

# read the log file
with open(inputFile, 'rt') as f:
    data = f.readlines()

# create the output directory if it doesn't exist
os.makedirs(os.path.dirname(outputFile), exist_ok=True)

def searchFor(searchQuery):
    for line in data:
        if line.__contains__(searchQuery):
            print(line)
            dataLog.append(line)
            with open(outputFile, 'a') as newFile:
                newFile.write(line)
    return dataLog

searchFor(ip)
print(f'{ip} found {len(dataLog)} times')

# search again for another string
searchQuery = input('Narrow it down, next string:')

def narrowDown():
    for line in dataLog:
        if line.__contains__(searchQuery):
            print(line)
narrowDown()
