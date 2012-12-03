import logging
import random
import numpy as np
from pprint import pprint
import matplotlib.pyplot as plt


v = False
v2=True
def run(p,k):
  randArr = np.array(random.sample(xrange(p), k))

  if v:
    pprint(randArr)

  dtype = [('h_val', int),('idx', int)]

  hashVal = np.zeros(k,dtype=dtype)
  countArr = np.zeros(k)

  total_hash = np.multiply(p,p-1).astype(float)
  for a in xrange(1,p):
    for i in xrange(0,k):
      hashVal['idx'][i] = i
      hashVal['h_val'][i] = np.mod(np.multiply(a,randArr[i]),p)

    sortedVal = np.sort(hashVal, order='h_val') #increasing order

    if v:
      print "sortedVal: "
      pprint(sortedVal)
      print "\n"

    hash_min = sortedVal['h_val'][0]
    hash_max = sortedVal['h_val'][k-1]

    countArr[sortedVal['idx'][0]]=countArr[sortedVal['idx'][0]]+p-hash_max+hash_min

    for j in xrange(1,k):
      countArr[sortedVal['idx'][j]]=countArr[sortedVal['idx'][j]]+sortedVal['h_val'][j]-sortedVal['h_val'][j-1]

    if v:
      print "current countArr: "
      pprint(countArr)
  
  if v2:
    print "FINAL COUNT"
    pprint(countArr)

  f1 = countArr.min().astype(float)/total_hash
  f2 = countArr.max().astype(float)/total_hash
  
  print "f1: "+str(f1)
  print "f2: "+str(f2)

  return (f1,f2)

def main():
  logging.basicConfig(format='%(asctime)s %(message)s')
  logging.warning('started')
  p = 49937
  k = 16
  ITR = 1000
  f1Arr = np.zeros(ITR)
  f2Arr = np.zeros(ITR)

  for it in xrange(0,ITR):
    r_val = run(p, k)
    f1Arr[it] = r_val[0]
    f2Arr[it] = r_val[1]
  
  plt.plot(f1Arr,'r--',f2Arr, 'b--')
  plt.show()

  logging.basicConfig(format='%(asctime)s %(message)s')
  logging.warning('ended')


main()