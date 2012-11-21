import logging
import random
import numpy
from scipy.weave import inline
from pprint import pprint

#macro
v = False
v2 = False
v3 = True
t = True
server = False

loc = '/Users/yifanwu/Dropbox/C3F/CS222/HW3/data/'
# the random number selector for set k given p (upper bound)
def getK(p,k):
  return random.sample(xrange(p), k)

def naiveHash(a,b,x,p):
  return (a*x+b)%p


def maxNmin(p, k):
  # p1 = 49937 and k = 16, 64, and 256
  k_set = getK(p, k)
  if t:
    pprint(k_set)
  min_count = [0] * k  
  #hash_dict = {}
  for a in xrange(1,p):
    if v:
      print "a: "+str(a)
        
    for b in xrange(0,p):
      if v:
        print "b: "+str(b)

      hash_min = (p+1,p) #reset  
      
      for i in xrange(0,k):
        ele = k_set[i]
        hash_val = naiveHash(a, b, ele, p)
        if v3 and (a==1):
            print str(hash_val)
  
        if hash_val < hash_min[1]:
          hash_min = (i,hash_val)
          if v:
            print "min: "+str(hash_min[1])

      min_count[hash_min[0]] = min_count[i] + 1  
    if v3 and (a==1):
      pprint(min_count)        

  if t:
    pprint(min_count)

  sorted_count = sorted(min_count)
  total_hash = (p-1)*p
  if v2:
    pprint(sorted_count)
    print str(total_hash)
  frac_min = float(sorted_count[0])/float(total_hash)
  frac_max = float(sorted_count[-1])/float(total_hash)
  return (frac_min,frac_max)

def main():
  logging.basicConfig(format='%(asctime)s %(message)s')
  logging.warning('started')
  
  p = 49937
  k = 16
  num_iter = 1000
  if t:
    p = 10
    k = 5
    num_iter = 1

  
  add = ""
  if server:
    add = 'Q4test.csv'
  else:
    add = loc+'Q4test.csv'
  f_s = open(add,'w+')
  f_s.write('min_frac,max_frac\n')

  for x in xrange(0,num_iter):
    result_tuple = maxNmin(p, k)
    c_min = str(result_tuple[0])
    c_max = str(result_tuple[1])
    print "min: "+c_min+"\t"+"max: "+c_max
    f_s.write(c_min+","+c_max+"\n")

  logging.basicConfig(format='%(asctime)s %(message)s')
  logging.warning('ended')
main()

################ TESTS ################
def test():
  x = 1
  y = 2
  print float(x)/float(y)

#test()