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

def capture(capturename):
    filename = capturename + '.json'
    samples = []
    print('Capturing...')
    starttime = datetime.now()
    try:
        while True:
            istat = requests.get('http://localhost:4027/api/')
            timestamp = datetime.now() - starttime
            samples.append({'timestamp': timestamp / timedelta(seconds=1),
                            'istatistica': json.loads(istat.text)})
            sleep(1)
    except: #Exception as e:
        #print_exc()
        pass
    print('Saving to file...')
    f = open(filename, 'w')
    json.dump(samples, f)
    system('chown "$(logname)" "' + filename + '"')
    print('Saved capture. Run ./macplot p ' + capturename + ' to plot.')

capture(starttime.strftime('%Y-%m-%d_%H-%M-%S'))
