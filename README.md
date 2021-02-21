# MacPlot

A tool for logging CPU & GPU frequencies, temperatures
and fan speeds as well as plotting them.

Currently only M1 Macs are supported, but if you want support for another device
that you have, feel free to open an Issue with the output of the following
shell commands (make sure you have iStatistica installed):
```
curl http://localhost:4027/api/
sudo powermetrics -i 1000 -n 1
sudo spindump 1 1 1000 -onlyTarget -stdout -noFile -noBinary
```
Or just implement it by yourself and make a PR.

## How to

At the moment we're using iStatista's API for getting all of the required
information, so you will need it: https://www.imagetasks.com/istatistica/pro/

Make sure you have the PIP3 package `requests` installed.

Just clone and cd, then run `./macplot c` and press ctrl-c when you're done.

Make sure you have the Numbers app installed.

Then run `./macplot p [cap]` where `[cap]` is the name of the capture, for
example `2021-02-21_13-06-49`.

If you want to install it, you can also run `sm install`.
