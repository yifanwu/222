import random
import numpy as np

T_SIZE = 500
TRIAL = 100
Stm = 383350 #\sum_{i=1}^{100}(i^2) = 338,350 + \sum_{j=1}^{9}\cdot 100 = 45,000
TH =  3834
CON = True #conservative update mode
v = False #testing
v1 = False

#global
hashVal = [{},{},{},{}]
flow = set()
c_tab = np.zeros((4,T_SIZE),dtype=np.int)
  

def update(update_val,ele,mode):
  global hashVal,flow,c_tab
  
  cur_min = Stm # maximum
  pos_l =[]

  for h in xrange(0,4):
    if(mode !=2):  
      pos = hashVal[h][ele] = random.randint(0, T_SIZE-1) #note: inclusive
    else:
      pos = hashVal[h][ele]

    pos_l.append(pos)
    cur_c = c_tab[h][pos] 
    if (cur_c < cur_min):
      cur_min = cur_c
  
  cur_min = cur_min + update_val
  
  for h in xrange(0,4):
    if (CON):
      c_tab[h][pos_l[h]] = max(c_tab[h][pos_l[h]],cur_min)
    else:
      c_tab[h][pos_l[h]] = c_tab[h][pos_l[h]] + update_val

  if (cur_min > TH):
    flow.add(ele)
    if v:
      print "Added is: "+str(ele)  
  
def run(mode): #1-forward,2-back,3-rand
  
  global hashVal,flow,c_tab
  
  if v:
    print "Running"
  
  #reset
  hashVal = [{},{},{},{}]
  flow = set()
  c_tab = np.zeros((4,T_SIZE),dtype=np.int)
  
  if (mode == 0):
    if v:
      print "In Forward Mode\n"
    for i in xrange(1,10):
      for j in xrange(1,1001):
        ele = 1000*(i-1)+ j
        update_val = i
        result = update(update_val, ele,mode)
    for k in xrange(1,101):
      ele = 9000+k
      update_val = k*k
      result = update(update_val, ele,mode)
  
  elif (mode == 1):
    if v:
      print "In BACK Mode\n"
    
    for k in xrange(100,0,-1):
      ele = 9000+k
      update_val = k*k
      result = update(update_val, ele,mode)
    for i in xrange(9,0,-1):
      for j in xrange(1000,0,-1):
        ele = 1000*(i-1)+ j
        update_val = i
        result = update(update_val, ele,mode)

  else:
    if v:
      print "In RANDOM Mode\n"
    
    valTab = np.zeros(Stm, dtype=np.int)

    count = 0
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
      print "RANDOM HAS ERROR"
      return

    np.random.shuffle(valTab)

    if v:
      print "Rand Count is: "+str(count)+" And total is: "+str(np.sum(valTab))

    for a in xrange(0,Stm):
      
      ele = valTab[a] 
      if v1:
        print "Current Element is: "+str(ele)

      if hashVal[0].get(ele) is None:
        for h in xrange(0,4):
          hashVal[h][ele] = random.randint(0, T_SIZE-1) #note: inclusive
      
      update(1, ele,mode)

  found_num = len(flow)
  print "\n"+str(mode)+": Occurance of the 1%: "+str(found_num)

  cur_max = Stm
  for h in xrange(0,4):
    cur = c_tab[h][hashVal[h][9100]]
    if (cur < cur_max):
      cur_max = cur
  print str(mode)+": 9100 showed up:"+str(cur_max)+"\n"

  return (found_num,cur_max)

def main():
  result = np.zeros((3,2),dtype=np.int)
  
  for mode in xrange(0,3):
    print "\n\nMODE: "+str(mode)+"\n"

    for a in xrange(0,TRIAL):
      r_tup = run(mode)
      result[mode][0] = result[mode][0] + r_tup[0]
      result[mode][1] = result[mode][1] + r_tup[1]

    ave_flow = float(result[mode][0])/float(TRIAL)
    ave_9100 = float(result[mode][1])/float(TRIAL)
    print "FOR MODE"+str(mode)+" FLOW: "+str(ave_flow)+" Element 9100 occures: "+str(ave_9100)+"\n"

main()