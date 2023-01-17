Executable File  3 lines (3 sloc)  154 Bytes

#!/bin/bash
# Bash scripts that sends a POST request to a given URL.
curl -s -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
