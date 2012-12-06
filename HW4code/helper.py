import numpy as np
import scipy as sc
from scipy import linalg
from pprint import pprint

v = False

'''
c_l = [1,2,3,4,5,6]
b = np.array([15,13,22,24,1,22])
A_v = np.zeros(4, dtype=np.int)
A = np.zeros((4,4), dtype=np.int)
'''

def RSC():
    #P(1) = 15,P(2) = 13,P(3) = 22,P(4) = 24,P(5) = 1,P(6) = 22
    count = 0
    for c in c_l:        
        if c != 0:
            A_v[count] = b[c-1]
            for y in xrange(0,4):
                A[count][y] = np.power(c,y)
            count += 1
    if v:
        print "\nSolving Now\n"
        pprint(A)
        pprint(A_v)
    r = linalg.solve(A, A_v)
    pprint(r)

def runRSC():
    global c_l

    for x in xrange(0,6):
        for y in xrange(x+1,6):
            c_l[x] = 0
            c_l[y] = 0
            RSC()
            c_l = [1,2,3,4,5,6]


########################

def coinBSC(k,p):
    val = np.float32(0.0)
    l_b = int(k+1)
    u_b = int(2*k+2)
    for i in xrange(l_b,u_b):
        ele = np.divide(sc.misc.factorial(2*k+1),np.multiply(sc.misc.factorial(2*k+1-i),sc.misc.factorial(i)))
        if v: print ele
        ele *= np.multiply(np.power((1-p),i),np.power(p,2*k-i+1))
            #c{{ \choose i}(1-p)^ip^{2k+1-i}}
        #np.power(p,exponent)
        if v: print ele
        val += ele#np.divide(,np.add(np.power(p,2*(k-i)+1),np.power((1-p),2*(k-i)+1)))

    print 1-val

def runBSC():
    for k in xrange(1,7):
        print "K is: "+str(k)
        coinBSC(k,0.1)
        print "\n"

runBSC()

