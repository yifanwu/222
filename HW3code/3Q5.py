import random
#from sets import set
import numpy as np

T_SIZE = 500
TRIAL = 100
Stm = 383350 #\sum_{i=1}^{100}(i^2) = 338,350 + \sum_{j=1}^{9}\cdot 100 = 45,000
TH =  3834

v = False
v2 = False
v3 = True
CON = True

#global
hashVal = [{},{},{},{}]
flow = set()
c_tab = np.zeros((4,T_SIZE),dtype=np.int)
  

def update(update_val,ele):
  cur_min = Stm # maximum
  pos_l =[]

  for h in xrange(0,4):
    pos = hashVal[h][ele] = random.randint(0, T_SIZE-1) #note: inclusive
    pos_l.append(pos)
    cur_c = c_tab[h][pos] 
    if (cur_c < cur_min):
      cur_min = cur_c
  
  cur_min = cur_min + i
  
  for h in xrange(0,4):
    if (CON):
      c_tab[h][pos_l[h]] = max(c_tab[h][pos_l[h]],cur_min)
    else:
      c_tab[h][pos_l[h]] = c_tab[h][pos_l[h]] + i

  if (cur_min > TH):
    flow.add(ele)
    if v:
      print "Added is: "+str(ele)  
  
def forward_n():
  hashVal = [{},{},{},{}]
  flow = set()

  c_tab = np.zeros((4,T_SIZE),dtype=np.int)
  
  for i in xrange(1,10):
    for j in xrange(1,1001):
      ele = 1000*(i-1)+ j
      if v2:
        print "Current element is: "+str(ele)
      result = update(hashVal, c_tab, flow, update_val, ele)

      
  for k in xrange(1,101):
    ele = 9000+k
    if v2:
        print "Current element is: "+str(ele)
    cur_min = Stm # maximum
      
    for h in xrange(0,4):
      pos = hashVal[h][ele] = random.randint(0, T_SIZE-1)
      cur_c = c_tab[h][pos] = c_tab[h][pos] + k*k
      if v2:
          print "has pos: "+str(pos)+" with value "+str(cur_c)
      if (cur_c<cur_min):
          cur_min = cur_c

    if (cur_min > TH):
        flow.add(ele)
        if v:
          print "Added is: "+str(ele)
  
  found_num = len(flow)
  print found_num

  cur_max = Stm
  for h in xrange(0,4):
    cur = c_tab[h][hashVal[h][9100]]
    if (cur < cur_max):
      cur_max = cur
  print "9100 showed up:"+str(cur_max)

  return (found_num,cur_max)

  
def backward_n():
  hashVal = [{},{},{},{}]
  flow = set()

  c_tab = np.zeros((4,T_SIZE),dtype=np.int)
  
  for k in xrange(100,0,-1):
    if v2:
      print k
    ele = 9000+k
    if v2:
        print "Current element is: "+str(ele)
    cur_min = Stm # maximum
      
    for h in xrange(0,4):
      pos = hashVal[h][ele] = random.randint(0, T_SIZE-1)
      cur_c = c_tab[h][pos] = c_tab[h][pos] + k*k
      if v2:
          print "has pos: "+str(pos)+" with value "+str(cur_c)
      if (cur_c<cur_min):
          cur_min = cur_c

    if (cur_min > TH):
        flow.add(ele)
        if v:
          print "Added is: "+str(ele)
  
  for i in xrange(9,0,-1):
    for j in xrange(1000,0,-1):
      ele = 1000*(i-1)+ j
      if v2:
        print "Current element is: "+str(ele)
      cur_min = Stm # maximum
      for h in xrange(0,4):
        pos = hashVal[h][ele] = random.randint(0, T_SIZE-1) #note: inclusive
        cur_c = c_tab[h][pos] = c_tab[h][pos] + i
        if v2:
          print "has pos: "+str(pos)+" with value "+str(cur_c )
        if (cur_c<cur_min):
          cur_min = cur_c

      if (cur_min > TH):
        flow.add(ele)
        if v:
          print "Added is: "+str(ele)
      
  found_num = len(flow)
  print "Number of low in 1%: "+str(found_num)

  cur_max = Stm
  for h in xrange(0,4):
    cur = c_tab[h][hashVal[h][9100]]
    if (cur < cur_max):
      cur_max = cur
  print "9100 showed up:"+str(cur_max)
    
  return (found_num,cur_max)


def random_n():
  hashVal = [{},{},{},{}]
  flow = set()
  valTab = np.zeros(Stm)
  count = 0
  c_tab = np.zeros((4,T_SIZE),dtype=np.int)
  
  for i in xrange(1,10):
    for j in xrange(1,1001):
      for b in xrange(1,i+1):
        valTab[count] = 1000*(i-1)+ j
        count = count + 1

  for k in xrange(1,101):
    k2 = k*k
    for c in xrange(1,k2+1):
      valTab[count] = 9000+k
      count = count + 1
  
  if (count != Stm):
    return

  np.random.shuffle(valTab)

  if v3:
    print str(valTab[0])

  for a in xrange(0,Stm):
    ele = valTab[a]
    cur_min = Stm # maximum
    if hashVal[0].get(ele) is None:
      for h in xrange(0,4):
        hashVal[h][ele] = random.randint(0, T_SIZE-1) #note: inclusive
    
    for h in xrange(0,4):  
      pos = hashVal[h][ele]
      cur_c = c_tab[h][pos] = c_tab[h][pos] + 1
      if v2:
        print "has pos: "+str(pos)+" with value "+str(cur_c )
      if (cur_c<cur_min):
        cur_min = cur_c

    if (cur_min > TH):
      flow.add(ele)
      if v:
        print "Added is: "+str(ele)
      
  found_num = len(flow)
  print "Number of low in 1%: "+str(found_num)

  cur_max = Stm
  for h in xrange(0,4):
    cur = c_tab[h][hashVal[h][9100]]
    if (cur < cur_max):
      cur_max = cur
  print "9100 showed up:"+str(cur_max)

  return (found_num,cur_max)


def main():
  #result = np.zero((3,2),dtype=np.int)
  back_max = back_flow = for_max = for_flow = rand_flow = rand_max = 0
  
  print "\n\nFORWARD\n"
  for a in xrange(0,100):
    f_r = forward_n()
    for_flow = for_flow + f_r[0]
    for_max = for_max + f_r[1]
  
  print "\n\nBACKWARD\n"  
  for a in xrange(0,100):  
    b_r = backward_n()
    back_flow = back_flow + b_r[0]
    back_flow = back_flow + b_r[1]
  
  print "\n\nRANDOM\n"  
  for a in xrange(0,100):  
    r_r = random_n()
    rand_flow = rand_flow + r_r[0]
    rand_flow = rand_flow + r_r[1]

  print "forward flow: "+str(for_flow/100)+" 9100 appearance "+str(for_max/100)
  print "back flow: "+str(back_flow/100)+" 9100 appearance "+str(back_max/100)
  print "rand flow: "+str(rand_flow/100)+" 9100 appearance "+str(rand_max/100)

#main()
#forward_n()
#backward_n()
random_n()