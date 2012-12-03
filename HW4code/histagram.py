#import numpy as np
import matplotlib.pyplot as plt
from pprint import pprint

def hash_plot():
    loc_3_hash = 'sorted_3_hash.txt'
    x=[]
    with open(loc_3_hash) as f:
        for line in f:
            val = int(line.strip())
            val /= 100
            x.append(val*100)

    #pprint(x)

    plt.hist(x)
    #, bins=(0,1000,2000,3000,4000))
    #np.histogram
    #, bins=10 #range=None, normed=False, weights=None,
    #       cumulative=False, bottom=None, histtype='bar', align='mid',
     #      orientation='vertical', rwidth=None, log=False,
      #     color=None, label=None, stacked=False,hold=None)

    plt.show()

hash_plot()

def test_plot():
    x = [1,1,1,2,2,4,4,4,4,4,4,5,5,6,9]
    plt.hist(x)#, bins=(0,1000,2000,3000,4000))
    plt.show()

#test_plot()

    

