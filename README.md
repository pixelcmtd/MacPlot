# MacPlot

A tool for logging CPU & GPU frequencies, temperatures
and fan speeds as well as plotting them.

Currently only M1 Macs are supported, but if you want support for other devices,
feel free to open PRs.

## How to

At the moment we're using iStatistica's API for getting all of the required
information, so you will need it: https://www.imagetasks.com/istatistica/pro/
(also note that you will need the Sensors Plugin)

Make sure you have the PIP3 package `requests` and the Numbers app installed.

Just clone and cd, then run `./macplot` and press ctrl-c when you're done.
