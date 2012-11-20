#p1 = 49, 937 and k = 16, 64, and 256

#hashing
def l_hash(a,x,b,p):
  return (ax+b)%p

# helper function, probably not going to be needed
def shuffle():  
  from random import shuffle
  x = [[i] for i in range(10)]
  shuffle(x)

