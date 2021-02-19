#!/usr/bin/env python3
import json
from sys import argv
import csv
import subprocess

samples = json.load(open(argv[1] + '.json', 'r'))
w = csv.writer(open(argv[1] + '.csv', 'w'))

w.writerow(['time (s)', 'power (mW)', 'fan (rpm)'])

for sample in samples:
    row = [float(sample['timestamp']) / 1000]
    row.append(int([i for i in sample['powermetrics'] if i[0] == 'Package' and i[1] == 'Power'][0][2]))
    row.append(int([i for i in sample['spindump'] if i[0] == 'Fan' and i[1] == 'speed'][0][2]))
    w.writerow(row)


subprocess.run(['/bin/sh', '-c', 'open \'' + argv[1] + '.csv\''])
