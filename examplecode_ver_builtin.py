#!/usr/bin/env python
# coding: utf-8

import pprint
import csv
import os
import HQS

def make_inputlist(csvfilename):
    inputlist = []
    with open(csvfilename, 'r', encoding='utf-8-sig') as f:
        rdr = csv.reader(f)
        for lx, line in enumerate(rdr):
            if lx == 0 : 
                idx1,idx2,idx3,idx4 = line.index('timestamp'),\
                line.index('name'),line.index('packageName'),line.index('type')
            add =[line[idx1],line[idx2],line[idx3],line[idx4]]  
            inputlist.append(add)
    return inputlist

foldername = 'testfolder'
fnms = os.listdir(foldername)       
fnms.sort()   

inputlist = []
for fnm in fnms: 
    if fnm[-3:] == 'csv':
        inputlist += make_inputlist('testfolder\\'+fnm)

result = HQS.digital (inputlist, 'h', 8, 'section','dayofweek', '_mean')
result['grp40']
