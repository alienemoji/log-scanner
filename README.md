# log-scanner
A simple log scanner that searches for lines containing a given IP

To use:
- Add the log file you want to scan as inputFile
- Run script
- Enter the IP/string you want to search for, script will print all lines and create outputFile
- Enter a second string to narrow it down, script will print all lines from dataLog that contain 2nd string.

The outputFile is created after the first search, not the second "narrow it down" search, this is intentional.
