#!/usr/bin/env python3
import json
import subprocess
import re
import requests
from traceback import print_exc
from datetime import datetime, timedelta
from time import sleep

def system(cmd):
    return subprocess.run(['/bin/sh', '-c', cmd], capture_output=True).stdout

def strip_empty(l):
    return [i for i in l if len(i) > 0]

def sample():
    istat = requests.get('http://localhost:4027/api/')
    #l = system('powermetrics -i 1000 -n 1 | grep :').decode('utf-8').split('\n')
    #a = system('spindump 1 1 1000 -onlyTarget -stdout -noFile -noBinary')
    timestamp = datetime.now() - starttime
    return {'timestamp': timestamp / timedelta(seconds=1),
            'istatistica': json.loads(istat.text)}
    #powermetrics = [strip_empty(re.split('[: ]+', s)) for s in strip_empty(l)]
    #a = strip_empty(a.decode('utf-8').split('\n'))
    #a = [s for s in a if s.find('com.apple.') == -1]
    #spindump = [strip_empty(re.split('[: ]+', s)) for s in a]
    #return {'timestamp':    timestamp / timedelta(milliseconds=1),
    #        'powermetrics': powermetrics,
    #        'spindump':     spindump}

starttime = datetime.now()
capturename = starttime.strftime('%Y-%m-%d_%H-%M-%S')
filename = capturename + '.json'
samples = []

print('Capturing...')

try:
    while True:
        samples.append(sample())
        sleep(1)
except: #Exception as e:
    #print_exc()
    pass

print('Saving to file...')

f = open(filename, 'w')
json.dump(samples, f)
system('chown "$(logname)" "' + filename + '"')

print('Saved capture. Run ./macplot p ' + capturename + ' to plot.')
