#!/usr/bin/env python3
import json
from sys import argv
import csv
import subprocess
from functools import reduce

samples = json.load(open(argv[1] + '.json', 'r'))
w = csv.writer(open(argv[1] + '.csv', 'w'))

w.writerow(['time (s)', 'cpu (‰)', 'fan (rpm)', 'P-cluster temp (*10C)'])

for sample in samples:
    istat = sample['istatistica']
    temps = istat['sensors']
    temps = [temps[k] for k in temps.keys() if k.split(' ')[0] == 'pACC']
    temps = [int(i) for i in temps if i != '' and int(i) != 0]
    row = ['%.1f' % sample['timestamp']]
    row.append(int(istat['summary_cpuLoad'] * 1000))
    row.append(istat['sensors_fansData'].rstrip())
    row.append(int(reduce(lambda x, y: x + y, temps) / len(temps) * 10))
    w.writerow(row)

subprocess.run(['/bin/sh', '-c', 'open \'' + argv[1] + '.csv\''])
