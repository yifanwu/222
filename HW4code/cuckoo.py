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