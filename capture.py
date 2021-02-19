#!/usr/bin/env python3
import json
import subprocess
import re
from traceback import print_exc
from datetime import datetime

filename = datetime + '.json'
samples = []

def system(cmd):
    return subprocess.run(['/bin/sh', '-c', cmd], capture_output=True).stdout

def strip_empty(l):
    return [i for i in l if len(i) > 0]

def sample():
    l = system('powermetrics -i 1000 -n 1 | grep :').decode('utf-8').split('\n')
    powermetrics = [strip_empty(re.split('[: ]', s)) for s in strip_empty(l)]
    a = system('spindump 1 1 1000 -onlyTarget -stdout -noFile -noBinary')
    return {'timestamp':    datetime,
            'powermetrics': powermetrics,
            'spindump':     spindump}

try:
    while True:
        samples.append(sample())
except: #Exception as e:
    #print_exc()
    pass

f = open(filename, 'w')
json.dump(samples, f)
system('chown "$(logname)" "' + filename + '"')
