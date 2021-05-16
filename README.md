# MacPlot

A tool for logging CPU & GPU frequencies, temperatures
and fan speeds as well as plotting them.

Currently only M1 Macs are supported, but if you want support for another device
that you have, feel free to open an Issue with the output of the following
shell command (make sure you have iStatistica installed):
```
curl http://localhost:4027/api/
```
Or just implement it by yourself and make a PR.

## How to

At the moment we're using iStatista's API for getting all of the required
information, so you will need it: https://www.imagetasks.com/istatistica/pro/

Make sure you have the PIP3 package `requests` and the Numbers app installed.

Just clone and cd, then run `./macplot` and press ctrl-c when you're done.
