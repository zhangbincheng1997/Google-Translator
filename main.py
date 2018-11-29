#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
import re
import time
from translate import google_translate

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--input', help='srt directory')
parser.add_argument('--output', help='trans directory')
args = parser.parse_args()

input = args.input
output = args.output
if input == None:
    input = 'srt'
if output == None:
    output = 'trans'

if not os.path.exists(input):
    exit(0)

if not os.path.exists(output):
    os.makedirs(output)

files = os.listdir(input)

for file in files:
    if file.endswith('.srt'):
        srtpath = os.path.join(input, file)
        transpath = os.path.join(output, file)

        with open(srtpath, 'r') as f:
            lines = f.readlines()
            transcontent = ''
            for line in lines:
                flag = re.search('[a-zA-Z]', line)
                if flag != None:
                    gt = google_translate(flag.string)
                    ch = gt.translate()
                    transcontent = transcontent + line + ch + '\n'
                    time.sleep(0.1)
                else:
                    transcontent = transcontent + line
            print(transcontent)

        with open(transpath, 'w') as f:
            f.write(transcontent)

        time.sleep(10)
        print('wait......10s')
