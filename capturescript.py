import json
import subprocess
from sys import argv
import re
from traceback import print_exc

samples = []

def system(cmd):
    return subprocess.run(['/bin/sh', '-c', cmd], capture_output=True).stdout

def strip_empty(l):
    return [i for i in l if len(i) > 0]

def sample():
    l = system('powermetrics -i 1000 -n 1 | grep :').decode('utf-8').split('\n')
    return [strip_empty(re.split('[: ]', s)) for s in strip_empty(l)]

try:
    while True:
        samples.append(sample())
except: #Exception as e:
    #print_exc()
    pass

f = open(argv[1], 'w')
json.dump(samples, f)
