import string
import numpy as np
from numpy import genfromtxt
import matplotlib.pyplot as plt
import csv
from pprint import pprint

loc = '/Users/yifanwu/Dropbox/C3F/CS222/code/result/'

def Q4(k):
  f3Arr=[]
  f_r = open(loc+'3_cloud_nonprime.txt','r')
  reader = csv.reader(f_r, delimiter=',')
  result = np.array([[float(col) for col in row] for row in reader])

  val = 1.0/16.0
  f1Arr = np.array([row[0] for row in result])
  f2Arr = np.array([row[1] for row in result])

  off1 = f1Arr.sum()/len(f1Arr)
  print (off1-val)*16.0
  off2 = f2Arr.sum()/len(f2Arr)
  print (off2-val)*16.0
  
  for x in xrange(0,len(result)):
    f3Arr.append(1.0/16.0)
  
  plt.plot(f1Arr,'r--',f2Arr, 'b--',f3Arr,'g--')
  plt.show()

def Q5():
  f_r = open(loc+'Q5_rand.txt','r')
  reader = csv.reader(f_r, delimiter=',')
  result = np.array([[float(col) for col in row] for row in reader])

  f1Arr = np.array([row[0] for row in result])
  f2Arr = np.array([row[1] for row in result])

  off1 = f1Arr.sum()/len(f1Arr)
  print off1
  off2 = f2Arr.sum()/len(f2Arr)
  print off2
  
 
Q5()
#Q4(16)