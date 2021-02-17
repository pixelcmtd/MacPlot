file="$(date).json"
python3 capturescript.py "$file"
chown "$(logname)" "$file"
