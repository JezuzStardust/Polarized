#!/usr/bin/env python

import os
import sys
import re 

flag = sys.argv[1]
url = sys.argv[2] 

if not url:
    os.exit(-1)
re_expr = r'https://coolors.co/(\w+)-(\w+)-(\w+)-(\w+)-(\w+)-(\w+)-(\w+)-(\w+)'

finder = re.compile(re_expr)

results = finder.findall(url)

if flag == '0':
    match03 = r'\s*let s:gui_base03\s*=\s"#(\w+)"'
    match02 = r'\s*let s:gui_base02\s*=\s"#(\w+)"'
    match01 = r'\s*let s:gui_base01\s*=\s"#(\w+)"'
    match00 = r'\s*let s:gui_base00\s*=\s"#(\w+)"'
    match0 = r'\s*let s:gui_base0\s*=\s"#(\w+)"'
    match1 = r'\s*let s:gui_base1\s*=\s"#(\w+)"'
    match2 = r'\s*let s:gui_base2\s*=\s"#(\w+)"'
    match3 = r'\s*let s:gui_base3\s*=\s"#(\w+)"'
    matchers = [match03, match02, match01, match00, match0, match1, match2, match3]
elif flag == '1': 
    match_yellow = r'\s*let s:gui_yellow\s*=\s"#(\w+)"'
    match_orange = r'\s*let s:gui_orange\s*=\s"#(\w+)"'
    match_red = r'\s*let s:gui_red\s*=\s"#(\w+)"'
    match_magenta = r'\s*let s:gui_magenta\s*=\s"#(\w+)"'
    match_violet = r'\s*let s:gui_violet\s*=\s"#(\w+)"'
    match_blue = r'\s*let s:gui_blue\s*=\s"#(\w+)"'
    match_cyan = r'\s*let s:gui_cyan\s*=\s"#(\w+)"'
    match_green = r'\s*let s:gui_green\s*=\s"#(\w+)"'
    print('woowo')
    matchers = [match_yellow, match_orange, match_red, match_magenta, match_violet, match_blue, match_cyan, match_green]

    

input_file = open('Polarized.vim-template', 'r')
ouptut_file = open('Polarized.vim', 'w')

for line in input_file:
    for i, pattern in enumerate(matchers):
        match = re.match(pattern, line) 
        if match:
            print(results[0][i], i)
            line = line.replace(match.group(1), results[0][i])
    ouptut_file.write(line)


