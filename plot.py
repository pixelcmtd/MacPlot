import json
import matplotlib.pyplot as plt
from sys import argv

samples = json.load(open(argv[1], 'r'))
time = []
power = []
# TODO: store in json
current_time = 0

for sample in samples:
    time.append(current_time)
    power.append(int([i for i in sample if i[0] == 'Package' and i[1] == 'Power'][0][2]))
    current_time += 1

fig, ax = plt.subplots()
ax.plot(time, power)
ax.set(xlabel='time (s)', ylabel='power (mW)', title='MacPlot')
ax.grid()

fig.savefig("fig.png")
plt.show()
