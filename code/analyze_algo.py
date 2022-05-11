# -*- coding: utf-8 -*-
"""
Created on Wed Sep  1 17:13:10 2021


"""

#---------------------------------------------------3.1---------------------------------------------------

import numpy as np
import matplotlib.pyplot as plt

# evenly sampled time at 200ms intervals
#n = np.arange(0., 5., 0.2)
n=np.array([2**x for x in range(20)])

# red dashes, blue squares and green triangles
plt.yscale('log')
plt.xscale('log')
plt.plot(8*n, 4*n*np.log2(n), 2*n**2, n**3, 2**n)
plt.show()

#---------------------------------------------------3.35---------------------------------------------------
#==========C-3.35===========================
def compactList(A):
  compactA=[]
  lenA=len(A)
  if lenA==0: 
      return A  
  compactA.append(A[0])
  for i in range(1,lenA):
      if A[i]!=A[i-1]:
          compactA.append(A[i])          
  return compactA

def apendBtoA(A,B):
    for x in B:
        A.append(x)
        
        
def disjoint3(A,B,C):
  """Sort each, eliminate any doubles, triples, 
  etc, join, sort again, check for triples"""
  sA = sorted(A)                
  sB = sorted(B)    
  sC = sorted(C)   
  
  cA=compactList(sA)
  cB=compactList(sB)
  cC=compactList(sC)

  ABC=[]
  
  apendBtoA(ABC,cA)
  apendBtoA(ABC,cB)
  apendBtoA(ABC,cC)
  
  sABC=sorted(ABC)
    

  for j in range(2, len(sABC)):
    if ((sABC[j-1] == sABC[j]) 
    and (sABC[j-1] == sABC[j-2])) :
      return False  # found duplicate pair
  return True       # if we reach this, elements were unique

A=[2,3,3,3,6]
B=[89,7,3,7]
C=[100,200,3,67,67]
   
disjoint3(A,B,C) 

D=[2,3,3,3,6]
E=[89,7,3,7]
F=[100,200,30,67,67]
   
disjoint3(D,E,F) 




#---------------------------------------------------3.45---------------------------------------------------
    

def find_missing_num(S):
    list_total = list(range(len(S)+1))
    total = 1
    for x in list_total:
        total *= x+1
    for x in S:
        total /= x+1
    return int(total - 1)

find_missing_num([0,1,2,3,4,6,7,8,9])

def find_missing(S):
    total_list = list(range(len(S)+1))
    total = 1
    for x in total_list:
        total *= x+1
        
    for x in S:
        total /= x+1
        
    return int(total-1)

find_missing([0,1,2,3,4,6,7,8,9])



#---------------------------------------------------3.50---------------------------------------------------

#================Pr: C.50================
def OnSqPoly(A, x):
    degPoly=len(A)
    p=0
    for i in range(degPoly):
        powX=1
        for j in range(i):
            powX *=x
        p+=A[i]*powX
    return p

print(OnSqPoly([1,2,3], 3))    
#34
#-----------------------------------
def power(x, y):
    if(y == 0):
        return 1
    d = power(x, y>>1) #recurse
    if((y&1) == 0): #even
        return d*d  # Exponentiation by squaring
    else:           #odd
        return x*d*d # Odd ball

def OnLognPoly(A, x): 
    degPoly=len(A)
    p=0
    for i in range(degPoly):
        powX = power(x, i)
        p+=A[i]*powX
    return p

print(OnLognPoly([1,2,3], 3))  
#34
print(OnLognPoly([1,2,3,4], 3))  
#34
#-----------------------------------
def OnPoly(A, x): # Horner's method: O(n)
    degPoly=len(A)
    p=0
    powX=1/x
    for i in range(degPoly):
        powX *=x
        p+=A[i]*powX
    return p

print(OnPoly([1,2,3], 3))    
#34.0
    
def poly_mult(x, a_coeffs):
    # a0 + a1 * x + a2 * x^2 + a3 * x^3 + a4 * x^4
    x_tot = 1   # x_tot initialized to 1 since x^0 = 1
    total = 0
    for i in a_coeffs:
        total += i * x_tot 
        x_tot *= x      # cannot use power function - calculating x^n
    return total

poly_mult(5, [1,2,3])

#---------------------------------------------------3.54---------------------------------------------------

def find_max_rep(S):
    
    rep = [0] * 4*len(S)
    maxRep = 0
    maxNum = 0
    for i in range(len(S)):
        rep[S[i]] += 1
        if rep[S[i]] > maxRep:
            maxRep = rep[S[i]] 
            maxNum = S[i]
    return maxNum                                                                                                                                                                 

find_max_rep([1,2,5,6,7,20,3,4,3,1,2,3,2,2])

#---------------------------------------------------3.55---------------------------------------------------

import math as m
def prefix_average1(S):
  n = len(S)
  A = [0] * n                     # create new list of n zeros
  for j in range(n):
    total = 0                     # begin computing S[0] + ... + S[j]
    for i in range(j + 1):
      total += S[i]
    A[j] = total / (j+1)          # record the average
  return A

def prefix_average2(S):
  n = len(S)
  A = [0] * n                     # create new list of n zeros
  for j in range(n):
    A[j] = sum(S[0:j+1]) / (j+1)  # record the average
  return A

def prefix_average3(S):
  n = len(S)
  A = [0] * n                   # create new list of n zeros
  total = 0                     # compute prefix sum as S[0] + S[1] + ...
  for j in range(n):
    total += S[j]               # update prefix sum to include S[j]
    A[j] = total / (j+1)        # compute average based on current sum
  return A


#==3.55===PrefixAvg Timing
import timeit

S=range(1000)

N=4
S1T=[0]*N
S2T=[0]*N
S3T=[0]*N

for i in range(0,N,1):
    S=range(int(m.pow(10,i+1)))
    S1T[i]=timeit.timeit(stmt='prefix_average1(S)', 
                         setup='from _main_ import prefix_average1, S',
                         number=int(m.pow(10,i)))
    S2T[i]=timeit.timeit(stmt='prefix_average2(S)', 
                         setup='from _main_ import prefix_average2, S',
                         number=int(m.pow(10,i)))
    S3T[i]=timeit.timeit(stmt='prefix_average3(S)', 
                         setup='from _main_ import prefix_average3, S',
                         number=int(m.pow(10,i)))

import matplotlib.pyplot as plt 
X=[]
for i in range(4):
    X.append(int(m.pow(10,i+1)))
             
X   
#[10, 100, 1000, 10000]             
   
S1T[0:4]
#[1.3400000000274304e-05, 0.005874000000000379, 7.5530057, 8871.0583351]
S2T[0:4]    
#[1.1399999999994748e-05, 0.0009324000000008326, 0.732191199999999, 992.1475842]         
S3T[0:4]
# [4.300000000512227e-06,
#  0.00019690000000061048,
#  0.023367099999997976,
#  2.9146380000001955]


plt.xscale('log')
plt.yscale('log')
plt.plot(X,S1T[0:4],label="preavg1")
plt.plot(X,S2T[0:4],label="preavg2")
plt.plot(X,S3T[0:4],label="preavg3")

plt.legend()
plt.show()
#---------------------------------------------------3.56---------------------------------------------------

#3.56
def example1(S): #O(n)

  """Return the sum of the elements in sequence S."""
  n = len(S)
  total = 0
  for j in range(n):             # loop from 0 to n-1
    total += S[j]
  return total

def example2(S): #O(n)
  """Return the sum of the elements with even index in sequence S."""
  n = len(S)
  total = 0
  for j in range(0, n, 2):       # note the increment of 2
    total += S[j]
  return total
  
def example3(S): #O(n^2)
  """Return the sum of the prefix sums of sequence S."""
  n = len(S)
  total = 0
  for j in range(n):            # loop from 0 to n-1
    for k in range(1+j):        # loop from 0 to j
      total += S[k]
  return total

def example4(S): #O(n)

  """Return the sum of the prefix sums of sequence S."""
  n = len(S)
  prefix = 0
  total = 0
  for j in range(n):
    prefix += S[j]
    total += prefix
  return total

def example5(A, B):        #O(n^3)   # assume that A and B have equal length
  """Return the number of elements in B equal to the sum of prefix sums in A."""
  n = len(A)                  
  count = 0
  for i in range(n):          # loop from 0 to n-1
    total = 0
    for j in range(n):        # loop from 0 to n-1
      for k in range(1+j):    # loop from 0 to j
        total += A[k]
    if B[i] == total:
      count += 1
  return count


import timeit

S=range(1000)
A=[2,3,5,7.11]
B=range(30)


t1=timeit.timeit(stmt='example1(S)', 
                         setup='from _main_ import example1, S',
                         number=1)

t2=timeit.timeit(stmt='example2(S)', 
                         setup='from _main_ import example2, S',
                         number=1)

t3=timeit.timeit(stmt='example3(S)', 
                         setup='from _main_ import example3, S',
                         number=1)

t4=timeit.timeit(stmt='example4(S)', 
                         setup='from _main_ import example4, S',
                         number=1)

t5=timeit.timeit(stmt='example5(A,B)', 
                         setup='from _main_ import example5, A, B',
                         number=1)

print("t1: ", t1)
print("t2: ", t2)
print("t3: ", t3)
print("t4: ", t4)
print("t5: ", t5)


# -----Alternate
# ----------------------------------------------------------
# ----------------------------------------------------------
import time
import matplotlib.pyplot as plt 

class Prefix():
    def __init__(self):
        self._timer_array = []


    def timer(func):
        def wrapper(*args, **kwargs):
            before = time.time()
            for _ in range(20):
                func(*args, **kwargs)
            after = time.time()
            args[0]._timer_array.append((after-before)*100000)  #Note, since the first argument is self, this is how we access self
            print ('Total time is ', after-before)
        return wrapper
            
class SumTimer(Prefix):
    def __init__(self):
        super().__init__()
        
    def timer(func):
        def wrapper(*args, **kwargs):
            before = time.time()
            for _ in range(20):
                func(*args, **kwargs)
            after = time.time()
            args[0]._timer_array.append((after-before)*100000)  #Note, since the first argument is self, this is how we access self
            print ('Total time is ', after-before)
        return wrapper
    
    @timer
    def example1(self, S):
        """Return the sum of the elements in sequence S"""
        n = len(S)
        total = 0
        for j in range(n):  #loop from 0 to n-1
            total += S[j]
        return total
    
    @timer
    def example2(self, S):
        """Return the sum of the elements with even index in sequence S"""
        n = len(S)
        total = 0
        for j in range(0,n,2):  #note the increment of 2
            total += S[j]
        return total
    
    @timer
    def example3(self, S):
        """Return the sum of the prefix sums of sequence S"""
        n = len(S)
        total = 0
        for j in range(n):  #loop from 0 to n-1
            for k in range(1+j):  #loop from 0 to j
                total += S[k]
        return total
    
    @timer
    def example4(self, S):
        """Return the sum of the prefix sums of sequence S"""
        n = len(S)
        prefix = 0
        total = 0
        for j in range(n):  #loop from 0 to n-1
            prefix += S[j]
            total += prefix
        return total
    
    @timer    
    def example5(self, A, B):
        """Return the number of elements in B equal to the sum of prefix sums in A"""
        n = len(A)
        count = 0
        for i in range(n):  #loop from 0 to n-1
            total = 0
            for j in range(n):   #loop from 0 to n-1
                for k in range(1+j):   #loop from 0 to j
                    total += A[k]
            if B[i] == total:
                count += 1

        return count
        
    def _reset_timers(self):
        self._timer_array = []
        
    def test_timers(self, e_n = 5):
        results = {}
        for name, func in [('1',self.example1), ('2', self.example2), ('3', self.example3), ('4', self.example4), ('5', self.example5)]:
            for i in range(1, e_n):
                test_array = list(range(10**i))
                if name == '5': func(test_array, test_array)
                else: func(test_array)
            results[name] = self._timer_array
            self._reset_timers()
            
        x = list(map(lambda x: 10**x, range(1, e_n)))
        return x, results
        
        
s = SumTimer()
x, results = s.test_timers(4)  #Note, even at 4 it takes 454 seconds for the last step of example5.  Increase at your own risk!

for f in results.values():
    plt.plot(x, f)
plt.xscale('log')
plt.yscale('log')

        
    
#---------------------------------------------------3.57---------------------------------------------------
#P-3.57
def example1(S): #O(n)

  """Return the sum of the elements in sequence S."""
  n = len(S)
  total = 0
  for j in range(n):             # loop from 0 to n-1
    total += S[j]
  return total

def example2(S): #O(n)

  """Return the sum of the elements with even index in sequence S."""
  n = len(S)
  total = 0
  for j in range(0, n, 2):       # note the increment of 2
    total += S[j]
  return total
  
def example3(S): #O(n^2)
  """Return the sum of the prefix sums of sequence S."""
  n = len(S)
  total = 0
  for j in range(n):            # loop from 0 to n-1
    for k in range(1+j):        # loop from 0 to j
      total += S[k]
  return total

def example4(S): #O(n)

  """Return the sum of the prefix sums of sequence S."""
  n = len(S)
  prefix = 0
  total = 0
  for j in range(n):
    prefix += S[j]
    total += prefix
  return total

def example5(A, B):        #O(n^3)   # assume that A and B have equal length
  """Return the number of elements in B equal to the sum of prefix sums in A."""
  n = len(A)                  
  count = 0
  for i in range(n):          # loop from 0 to n-1
    total = 0
    for j in range(n):        # loop from 0 to n-1
      for k in range(1+j):    # loop from 0 to j
        total += A[k]
    if B[i] == total:
      count += 1
  return count


import timeit

S=range(1000)
A=[2,3,5,7.11]
B=range(30)


t1=timeit.timeit(stmt='example1(S)', 
                         setup='from _main_ import example1, S',
                         number=1)

t2=timeit.timeit(stmt='example2(S)', 
                         setup='from _main_ import example2, S',
                         number=1)

t3=timeit.timeit(stmt='example3(S)', 
                         setup='from _main_ import example3, S',
                         number=1)

t4=timeit.timeit(stmt='example4(S)', 
                         setup='from _main_ import example4, S',
                         number=1)

t5=timeit.timeit(stmt='example5(A,B)', 
                         setup='from _main_ import example5, A, B',
                         number=1)

print("t1: ", t1)
print("t2: ", t2)
print("t3: ", t3)
print("t4: ", t4)
print("t5: ", t5)

# t1:  0.00013920000000666732
# t2:  7.019999999613447e-05
# t3:  0.07624149999999474
# t4:  0.00028690000000608507
# t5:  1.650000000097407e-05
#---------------------------------------------------3.58---------------------------------------------------
#---------P3-58---------------------
import time

class Unique():
    NUM_TESTS_PER_TIMECHECK = 10000
    def __init__(self):
        pass
    
    def tests_per_minute(func):
        def wrapper(*args, **kwargs):
            total_time = 60  #For one minute
            counter = 0
            while total_time >= 0:
                before = time.time()
                for _ in range(args[0].NUM_TESTS_PER_TIMECHECK):
                    out = func(*args, **kwargs)
                after = time.time()
                total_time -= after-before
                counter += 1
                #print (total_time)
                
            num_tests = counter * args[0].NUM_TESTS_PER_TIMECHECK
            return  num_tests
        return wrapper


    @tests_per_minute
    def unique1(self, S):
        for j in range(len(S)):
            for k in range(j+1, len(S)):
                if S[j] == S[k]:
                    return False
        return True

    @tests_per_minute
    def unique2(self, S):
        temp = sorted(S)
        for j in range(1, len(temp)):
            if S[j-1] == S[j]:
                return False
        return True

    
    #Note, we need this to prevent the decorator from calling itself infinitely
    def uniquer(self, S, start = 0, stop = None):
        if stop is None: stop = len(S)
        if stop-start <= 1: return True
        elif not self.uniquer(S, start, stop-1): return False
        elif not self.uniquer(S, start+1, stop): return False
        else: return S[start] != S[stop-1]
    
    #This is from the next chapter...
    @tests_per_minute
    def unique3(self, S, start = 0, stop = None):
        if stop is None: stop = len(S)
        if stop-start <= 1: return True
        elif not self.uniquer(S, start, stop-1): return False
        elif not self.uniquer(S, start+1, stop): return False
        else: return S[start] != S[stop-1]
        
    def test_each_algo(self, n):
        S = list(range(n))
        num_tests = {}
        for name, func in [('Unique1', self.unique1), ('Unique2', self.unique2), ('Unique3', self.unique3)]:
            num = func(S)
            num_tests[name] = num
        return num_tests
    
    
n = 5
u = Unique()
#u.unique3([1,2,3,4,5,6])
results = u.test_each_algo(n)
for key, value in results.items():
    print (f"The total number of tests for {key} is {value} for n = {n}")
#---------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------
# alternate 3.58
#P-3.58
def unique1(S): #O(n^2)
  """Return True if there are no duplicate elements in sequence S."""
  for j in range(len(S)):
    for k in range(j+1, len(S)):
      if S[j] == S[k]:
        return False              # found duplicate pair
  return True                     # if we reach this, elements were unique

def unique2(S): #O(n(log(n)))
  """Return True if there are no duplicate elements in sequence S."""
  temp = sorted(S)                # create a sorted copy of S
  for j in range(1, len(temp)):
    if temp[j-1] == temp[j]:
      return False                # found duplicate pair
  return True                     # if we reach this, elements were unique

def unique3(S, start=0, stop=None): #O(2^n)
    """Return True if there are no duplicate elements in slice S[start:stop]."""
    if stop is None: stop = len(S)
    if stop-start <= 1: return True
    elif not unique3(S, start, stop-1): 
        return False # ﬁrst part has duplicate
    elif not unique3(S, start+1, stop): 
        return False # second part has duplicate
    else: 
        return S[start] != S[stop-1] 

    
import timeit

print("unique1 -------------------------------------")
for i in range(35000,40000,1000):
    S=list(range(i))
    t=timeit.timeit(stmt='unique1(S)', 
                         setup='from _main_ import unique1, S',
                         number=1)
    print("unique1 Interim:",i,t)
    if t>=60:
        print("unique1 Results:",i,t)
        break

    
print("unique2 -------------------------------------")
for i in range(400000000,1000000000,10000000):
    S=list(range(i))
    t=timeit.timeit(stmt='unique2(S)', 
                         setup='from _main_ import unique2, S',
                         number=1)
    print("unique2 Interim:",i,t)
    if t>=60:
        print("unique1 Results:",i,t)
        break

# unique2 -------------------------------------
# unique2 Interim: 400000000 52.8287788000016
# unique2 Interim: 410000000 55.62124519999634
# unique2 Interim: 420000000 60.45238490000338
# unique1 Results: 420000000 60.45238490000338

print("unique3 -------------------------------------")
for i in range(1,30,1):
    S=list(range(i))
    t=timeit.timeit(stmt='unique3(S)', 
                         setup='from _main_ import unique3, S',
                         number=1)    
    print("unique3 Interim:",i,t)    
    if t>=60:
        print("unique3 Results:",i,t)












