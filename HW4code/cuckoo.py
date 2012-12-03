from pprint import pprint
import random
import numpy as np


#macros
TAB_SIZE = 16384
MAX_TRIES = 100
MAX_RUN = 1000
NUM_HASH = 3
v = False
vv = False
t = False

if t:
    TAB_SIZE = 500
    MAX_TRIES = 10
    MAX_RUN = 2
    v = True
    vv = True


val_tab = np.zeros((TAB_SIZE,2),dtype=int)

if NUM_HASH is 2:
    hash_tab = [[],[]]
else:
    hash_tab = [[],[],[]]


def kick(kick_ele, original_loc):
    kick_count = MAX_TRIES
    if vv:
        pprint(hash_tab)

    while kick_count > 0:
        if v:
            print "On count: "+str(kick_count)
        
        hash_count = 0
        
        for y in xrange(0, NUM_HASH):
            kick_loc = hash_tab[y][kick_ele]
            if kick_loc != original_loc:
                hash_count += 1
                if v:
                   print "Kicking: current val is: "+str(val_tab[kick_loc][0])+" at positon "+str(kick_loc)+" with value "+str(val_tab[kick_loc][1])
            
                if val_tab[kick_loc][0] == 0:
                    val_tab[kick_loc][0] = 1
                    val_tab[kick_loc][1] = kick_ele
                    if v:
                        print "Good! Found a place to go"
                    return True
                else:
                    if hash_count == (NUM_HASH -1):
                        kick_ele = val_tab[kick_loc][1] 
                        original_loc = kick_loc
                        if v:
                            print "Kick element updated to "+str(kick_ele)
                        
            kick_count -= 1

    if v:
        print "Bad! No other place to go now!"
    return False




def cuckoo():
    global val_tab, hash_tab

    #reset
    val_tab = np.zeros((TAB_SIZE,2),dtype=int)

    if NUM_HASH == 2:
        hash_tab = [[],[]]
    else:
        hash_tab = [[],[],[]]



    #conceptually hash values indexed at 0, 1 ... until it stops
    input_count = 0
    #loop until
    while True:
        if v:
            print "Working on number: "+str(input_count)+" of input"
        #must be initialized in separate process 
        #to make sure that we could stop at the first one
        #to make sure that there are no repeats
        hash_val_set = random.sample(range(TAB_SIZE), NUM_HASH)

        for x in xrange(0,NUM_HASH):
            #hash_val = np.random.randint(TAB_SIZE)
            hash_tab[x].append(hash_val_set[x])

        for x in xrange(0,NUM_HASH):        
            loc = hash_tab[x][input_count]
            if v:
                print "Current value in table is: "+str(val_tab[loc][0])+" at location: "+str(loc)+" with value "+str(val_tab[loc][1])

            if val_tab[loc][0] == 0:
                if v:
                    print "Updating value!"
                # assign and we are done                
                val_tab[loc][0] = 1
                val_tab[loc][1] = input_count
                #stop and not update others
                break
            
            #first no mach
            else:
                if x == (NUM_HASH-1):
                    #last chance now need to kickout
                    if v:
                        print "Oh no, need to kick elements out now!"
                    kick_ele = val_tab[loc][1] 
                    if kick(kick_ele,loc) is False:
                        if v:
                            print "The final resulting table is: "
                            pprint(val_tab)
                        print "The number of elements filled is: "+str(input_count)
                        
                        return input_count
        if vv:
            pprint(val_tab)
        input_count += 1

def main():
    global NUM_HASH

    for j in xrange(2,4):
        NUM_HASH = j
        ave_val = 0        
        for i in xrange(0, MAX_RUN):
            ave_val += cuckoo()
        print "Average number of possible inputs "+str(ave_val/MAX_RUN)

if t:
    cuckoo()
else:
    main()


