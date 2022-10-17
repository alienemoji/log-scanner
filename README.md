# log-scanner

A simple log scanner that searches for lines containing a given IP or string and outputs the results to a .txt file for reporting or analysis.

## Usage:
`python3 scanner.py <FILENAME> <SEARCHQUERY> -printresults`

`python3 scanner.py auth.log 'Invalid user'` - Will search auth.log for lines containing the string "Invalid user"

## Command line arguments

- `FILENAME`: Log file to scan
- `SEARCHQUERY`: String or IP to search for
- `-printresults`: (Optional) Print results to terminal
