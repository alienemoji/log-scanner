# log-scanner

A simple log scanner that searches for lines containing a given IP or string and outputs the results to a .txt file for reporting or further analysis. Written when I noticed some novel traffic in my logs that I wanted to report to DigitalOcean but couldn't copy all of it manually.

## Usage:
`python3 scanner.py <FILENAME> <SEARCHQUERY> -printresults`

`python3 scanner.py auth.log 'Invalid user'` - Will search auth.log for lines containing the string "Invalid user"

## Command line arguments

- `FILENAME`: Log file to scan
- `SEARCHQUERY`: String or IP to search for
- `-printresults`: (Optional) Print results to terminal

### To do
- Write a function to block an IP with ufw/iptables if found >n times
- Take multiple search queries as input or read them from a .txt file
