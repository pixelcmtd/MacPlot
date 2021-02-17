sample() (powermetrics -i 1000 -n 1 --show-all -f plist)
plist2json() (python3 plist2json.py)

file="$(date).plist"
{
        echo -n '['
        while true ; do
                echo -n "$(sample | plist2json),"
        done
        echo -n ']'
} > "$file"
chown "$(logname)" "$file"
