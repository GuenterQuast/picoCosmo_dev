#!/usr/bin/python3
# -*- coding: utf-8 -*-
# script plotDoublePulses.py

'''create pictures in .png format from raw wave forms saved by picoCosmo.py
'''

from __future__ import print_function, division, unicode_literals
from __future__ import absolute_import

import sys, os, time, yaml, numpy as np
import zipfile

import matplotlib.pyplot as plt, matplotlib.animation as anim

# animated displays running as background processes/threads
from picodaqa.Oscilloscope import *

def readblock():
# read data sequentially from input file
#   end of block marked by ']]\n'
  global f
  txt = ''
  while True:
    if zipmode == True:
      l = f.readline().decode('utf-8')
    else:
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
    fname = sys.argv[1]
  else: 
    fname = 'rawDPtest.dat'
  print('    input from file ' + fname)

  try:
    # read from zip file
    if fname.split('.')[-1]=='zip':
      zipmode = True
      zf = zipfile.ZipFile(fname, 'r')
      fnam = zf.namelist()[0]  # first file
      print('    reading from packed file ' + fnam)
      f = zf.open(fnam)
    else:
    # read from unpacked file
      zipmode = False
      f = open(fname, 'r')
  except:
    print(' !!! failed to open input file ' + fname)
    exit(1)

  # read first block from file
  try:
    txt = readblock()   
    obj = yaml.load(txt)
    conf = obj['OscConf']
  except:
    print('     failed read oscillocope configuration ')
    exit(1)

  dirname = 'dpFigs'
  if not os.path.exists(dirname): 
          os.makedirs(dirname)

  print(" ** storing figures")
  plt.ion()  
  # initialize oscilloscope display
  Osci = Oscilloscope(conf, 'DoublePulse') 
  figOs = Osci.fig
  Osci.init()
  cnt = 0 
  
  while True:
    data = obj['data']
    for d in data:
      cnt += 1
      evt = (3, cnt, time.time(), d)
      print("  storing picture %i"%(cnt))
      Osci(evt)
      figOs.savefig(dirname + '/DPfig%03i'%(cnt)+'.png')

    txt = readblock()
    if txt == '':
      break # end of file
    obj = yaml.load('data: \n' + txt)
    data = obj['data']

  f.close()
  print(sys.argv[0] + " end *==*")
