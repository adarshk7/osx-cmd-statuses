#!/usr/bin/env python3

import subprocess

process = subprocess.Popen(
    ['osascript', '-e', 'get volume settings'], stdout=subprocess.PIPE
)

stdout = process.stdout.readline()
data = str(stdout[:-1]).replace("'", '').split(',')
output_volume = data[0].split(':')[-1]
input_volume = data[1].split(':')[-1]
muted = data[3].split(':')[-1]

print('{2}  {0}    🎤  {1}'.format(
    output_volume,
    input_volume, 
    '🔊' if muted == 'false' else '🔇'
))
