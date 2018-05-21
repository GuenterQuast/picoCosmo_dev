#!/usr/bin/python3
# -*- coding: utf-8 -*-
# script plotDoublePulses.py

'''visual display of raw wave forms saved by picoCosmo.py
'''

from __future__ import print_function, division, unicode_literals
from __future__ import absolute_import

import sys, time, yaml, numpy as np

import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt, matplotlib.animation as anim

# animated displays running as background processes/threads
from picodaqa.Oscilloscope import *

def readblock():
# read data sequentially from input file
#   end of block marked by ']]\n'
  global f
  txt = ''
  while True:
    l = f.readline()
    if (not l):  # end of file 
      # print('   end of file')
      return ''
    txt += l
    if l[-3:-1] == ']]':
      # print('   end of block')
      return txt 

if __name__ == "__main__": # -----------------------------

  print('\n*==* script ' + sys.argv[0] + ' running \n')
  if len(sys.argv)==2:
    fnam = sys.argv[1]
  else: 
    fnam = 'rawDPtest.dat'
  print('    input from file ' + fnam)

  try:
    f = open(fnam, 'r')
  except:
    print('     failed to open input file ' + fnam)
    exit(1)

  # read first block from file
  try:
    txt = readblock()   
    obj = yaml.load(txt)
    conf = obj['OscConf']
  except:
    print('     failed read oscillocope configuration ')
    exit(1)

  print("*= start animation")
  plt.ion()  
  # initialize oscilloscope display
  Osci = Oscilloscope(conf, 'DoublePulse') 
  figOs = Osci.fig
  Osci.init()
  twait = 0.3  # time between figure updates in s
  cnt = 0 
  
  while True:
    data = obj['data']
    for d in data:
      cnt += 1
      evt = (3, cnt, time.time(), d)
      print("event %i"%(cnt))
      Osci(evt)
      figOs.canvas.draw()
##    figOs.savefig('DPfig%03i'%(cnt)+'.png')
      time.sleep(twait)

    # read next block
    txt = readblock()
    if txt == '':
      break # end of file
    obj = yaml.load('data: \n' + txt)
    data = obj['data']

  f.close()
  print("*= end")
