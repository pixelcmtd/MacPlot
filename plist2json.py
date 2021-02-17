from json import dump
from plistlib import loads
from sys import stdin, stdout

dump(loads(stdin.read().encode("utf-8")), stdout)
