#-----------------------------------------------5.1-------------------------------------------------------------
#==============================================
import sys # provides getsizeof function
data = []
n=28
for k in range(n): # NOTE: must ﬁx choice of n
    a = len(data) # number of elements
    b = sys.getsizeof(data) # actual size in bytes
    print('Length: {0:3d}; Size in bytes: {1:4d}' .format(a, b))
    data.append(None) # increase length by one
    


#-----------------------------------------------5.2-------------------------------------------------------------
import sys
def array_jumps(n):
    data = []
    size_old = 0
    i = 0
    for _ in range(n):
        i += 1
        size = sys.getsizeof(data)
        if size != size_old:
            print(len(data), end = ', ')
        # print(i, len(data), sys.getsizeof(data))
        size_old = size
        data.append(None)
        
array_jumps(10000)

#-----------------------------------------------5.3-------------------------------------------------------------
import sys # provides getsizeof function
data = []
n=1000
size_old = sys.getsizeof(data)
for k in range(n): # NOTE: must ﬁx choice of n
    a = len(data) # number of elements
    b = sys.getsizeof(data) # actual size in bytes
    if b != size_old:
        print('Length: {0:3d}; Size in bytes: {1:4d}' .format(a, b))
    size_old = b
    data.append(None) # increase length by one
print('-----------------------------------------')
print('-----------------------------------------')
n = 900

for k in range(n): # NOTE: must ﬁx choice of n
    a = len(data) # number of elements
    b = sys.getsizeof(data) # actual size in bytes
    if b != size_old:
        print('Length: {0:3d}; Size in bytes: {1:4d}' .format(a, b))
    size_old = b
    data.pop() # increase length by one
    

#-----------------------------------------------5.4-------------------------------------------------------------
import ctypes                                      # provides low-level arrays

class DynamicArray:
  """A dynamic array class akin to a simplified Python list."""

  def __init__(self):
    """Create an empty array."""
    self._n = 0                                    # count actual elements
    self._capacity = 1                             # default array capacity
    self._A = self._make_array(self._capacity)     # low-level array
    
  def __len__(self):
    """Return number of elements stored in the array."""
    return self._n
    
  def __getitem__(self, k):
    """Return element at index k."""
    if ( 0 <= k < self._n):
        return self._A[k]                              # retrieve from array
    elif (-self._n <= k <= -1):
        k = self._n + k
        return self._A[k]                    # retrieve from array
    else:
      raise IndexError('invalid index')
  
  def append(self, obj):
    """Add object to end of the array."""
    if self._n == self._capacity:                  # not enough room
      self._resize(2 * self._capacity)             # so double capacity
    self._A[self._n] = obj
    self._n += 1

  def _resize(self, c):                            # nonpublic utitity
    """Resize internal array to capacity c."""
    B = self._make_array(c)                        # new (bigger) array
    for k in range(self._n):                       # for each existing value
      B[k] = self._A[k]
    self._A = B                                    # use the bigger array
    self._capacity = c

  def _make_array(self, c):                        # nonpublic utitity
     """Return new array with capacity c."""   
     return (c * ctypes.py_object)()               # see ctypes documentation

  def insert(self, k, value):
    """Insert value at index k, shifting subsequent values rightward."""
    # (for simplicity, we assume 0 <= k <= n in this verion)
    if self._n == self._capacity:                  # not enough room
      self._resize(2 * self._capacity)             # so double capacity
    for j in range(self._n, k, -1):                # shift rightmost first
      self._A[j] = self._A[j-1]
    self._A[k] = value                             # store newest element
    self._n += 1

  def remove(self, value):
    """Remove first occurrence of value (or raise ValueError)."""
    # note: we do not consider shrinking the dynamic array in this version
    for k in range(self._n):
      if self._A[k] == value:              # found a match!
        for j in range(k, self._n - 1):    # shift others to fill gap
          self._A[j] = self._A[j+1]
        self._A[self._n - 1] = None        # help garbage collection
        self._n -= 1                       # we have one less item
        return                             # exit immediately
    raise ValueError('value not found')    # only reached if no match
    
a = [1,2,3,4,5]
print(a[4])
print(a[-1])
print(a[-5])
print(a[-6])
da=DynamicArray() 
type(da)
for k in range(10):
    da.append(k)
da[9]
da[0]
da[-1]
#-----------------------------------------------5.5-------------------------------------------------------------
# alternate logic
"""
Problem R.5.5

If I triple the growing costs:

$1: For current write
$3: To copy me when I move house
$3: To copy all grandfathered items 
     when we move house 
==================================
$7
"""
#-----------------------------------------------5.6-------------------------------------------------------------
def append(self, obj):
    """Add object to end of the array."""
    if self._n == self._capacity:                  # not enough room
      self._resize(2 * self._capacity, obj,self._n) # so double capacity
    else:
      self._A[self._n] = obj
    self._n += 1

def _resize(self, c,value,k):                    # nonpublic utitity
    """Resize internal array to capacity c."""
    B = self._make_array(2 * self._capacity)     # I: so double capacity
    for i in range(k):                           # II: Xfer the pre-k
        B[i] = self._A[i]
        B[k] = value                             # III: Plunk in the new kid at k 
    for i in range(self._n, k, -1):               # IV: Xfer post-k items 
        B[i] = self._A[i-1]
    self._A = B                                  # use the bigger array
    self._capacity = c        

def _make_array(self, c):                        # nonpublic utitity
     """Return new array with capacity c."""   
     return (c * ctypes.py_object)()               # see ctypes documentation

def insert(self, k, value):
    """Insert value at index k, shifting subsequent values rightward."""
    # (for simplicity, we assume 0 <= k <= n in this verion)
    if self._n == self._capacity:                  # not enough room
      self._resize(2 * self._capacity,value,k)             # O: so double capacity
    else:                   
      for j in range(self._n, k, -1):               
        self._A[j] = self._A[j-1]
      self._A[k] = value                             # IV: store newest element
    self._n += 1

#-----------------------------------------------5.7-------------------------------------------------------------
# O(n)
# Sum - (n-1)*n/2 will give repeated int
#-----------------------------------------------5.8-------------------------------------------------------------
import sys
from time import time

for N in [100, 1000, 10000, 100000, 1000000]:
    start = time()  
    data=list(range(1000000))
    for n in range(N):
        data.pop(0) #begin        
    end = time()                   # record the end time (in seconds)
    avgTimeComp=(end - start) / N       # compute average per operation
    print('At Begin, Average of {0:.3f} for n {1}'.format(avgTimeComp*1000000, N))

    start = time()  
    data=list(range(1000000))    
    for n in range(N):
        data.pop(len(data)//2) #middle
    end = time()                   # record the end time (in seconds)
    avgTimeComp=(end - start) / N       # compute average per operation
    print('AT Middle, Average of {0:.3f} for n {1}'.format(avgTimeComp*1000000, N))
        
    start = time()  
    data=list(range(1000000))    
    for n in range(N):
        data.pop() #end
    end = time()                   # record the end time (in seconds)
    avgTimeComp=(end - start) / N       # compute average per operation
    print('At End, Average of {0:.3f} for n {1}'.format(avgTimeComp*1000000, N))
#-----------------------------------------------5.9-------------------------------------------------------------

class CaesarMultiLangaugeCipher:
  """Class for doing encryption and decryption using a Caesar cipher."""

  def __init__(self, shift, language='English'):
    """Construct Caesar cipher using given integer shift for rotation."""
    self._numchars = 26
    self._first_language_letter = ord('\u0410')
    if language.upper() == 'ENGLISH':
        self._numchars = 26
        self._first_language_letter = ord('A')
    elif language.upper() == 'GREEK':
        self._numchars = 25
        self._first_language_letter = ord('\u0391')
    elif language.upper() == 'RUSSIAN':
        self._numchars = 32
        self._first_language_letter = ord('\u0410')
        
    encoder = [None] * self._numchars                           # temp array for encryption
    decoder = [None] * self._numchars                           # temp array for decryption
    for k in range(self._numchars):
      encoder[k] = chr((k + shift) % self._numchars + self._first_language_letter)
      decoder[k] = chr((k - shift) % self._numchars + self._first_language_letter)
    self._forward = ''.join(encoder)                # will store as string
    self._backward = ''.join(decoder)               # since fixed
    #print(self._forward)
    #print(self._backward)

  def encrypt(self, message):
    """Return string representing encripted message."""
    return  self._transform(message, self._forward)

  def decrypt(self, secret):
    """Return decrypted message given encrypted secret."""
    return  self._transform(secret, self._backward)

  def _transform(self, original, code):
    """Utility to perform transformation based on given code string."""
    msg = list(original)
    for k in range(len(msg)):
      if msg[k].isupper():
        j = ord(msg[k]) - self._first_language_letter                  # index from 0 to 25
        #print(code)
        #print('j', j)
        msg[k] = code[j]                            # replace this character
    return ''.join(msg)

if __name__ == '__main__':
  cipher = CaesarMultiLangaugeCipher(10, 'Russian')
  message = "ОРЕЛ ЕСТЬ"
  coded = cipher.encrypt(message)
  print('Secret: ', coded)
  answer = cipher.decrypt(coded)
  print('Message:', answer)
  
  cipher2 = CaesarMultiLangaugeCipher(10, 'Greek')
  message = "ΑΒΓ ΔΕΖ ΗΘΙ ΚΛΜ; ΝΞΟ ΠΡΣ ΤΥΦ ΧΨ'Ω."
  coded = cipher2.encrypt(message)
  print('Secret: ', coded)
  answer = cipher2.decrypt(coded)
  print('Message:', answer)

  cipher3 = CaesarMultiLangaugeCipher(10, 'English')
  message = "EAGLE HAS LANDED"
  coded = cipher3.encrypt(message)
  print('Secret: ', coded)
  answer = cipher3.decrypt(coded)
  print('Message:', answer)


#-----------------------------------------------5.10-------------------------------------------------------------
def ConstructACeaserSalad(shift):
    """Construct Caesar cipher using given integer shift for rotation."""
    numchars = 26
    first_language_letter = ord('A')
    forward = ''.join([ chr((k + shift) % numchars + first_language_letter) for k in range(numchars)])              
    backward = ''.join([ chr((k - shift) % numchars + first_language_letter) for k in range(numchars)])          
    print(forward ) #,,--Just for reference
    print(backward )

ConstructACeaserSalad(3)

#DEFGHIJKLMNOPQRSTUVWXYZABC
#WXYABCDEFGHIJKLMNOPQRSTUVW
#-----------------------------------------------5.11-------------------------------------------------------------
def SumAllNums(N):
    ## expecting N to be n * n matrix - compute sum
    total = 0
    for i in range(len(N)):
        for j in range(len(N[0])):
            total += N[i][j]
    print(total)
    
if __name__ == '__main__':
    N = [ [j]* 5 for j in range(4) ]
    print(N)
    SumAllNums(N)
#-----------------------------------------------5.12-------------------------------------------------------------
def sum_2d_w_sum(array):
    return sum([sum(i) for i in array])

#-----------------------------------------------5.13-------------------------------------------------------------
import sys

def test_no_init(n):
    data = []
    for k in range(n):
        a = len(data)
        b = sys.getsizeof(data)
        #print('Length: {0:3d}; Size in bytes: {1:4d}'.format(a,b))
        print(a, b)
        data.append(None)

def test_with_init(n, m):
    data = [None] * m
    for k in range(n-m):
        a = len(data)
        b = sys.getsizeof(data)
        #print('Length: {0:3d}; Size in bytes: {1:4d}'.format(a,b))
        print(a, b)
        data.append(None)
        
if __name__ == '__main__':
    test_no_init(200)
    test_with_init(200, 100)

    
#-----------------------------------------------5.14-------------------------------------------------------------
import random
a = ['a','b','c','d','e']


z = []
s = []
for j in range(len(a)):
    b = random.randrange(0, len(a))
    while b in s:
        b = random.randrange(0, len(a))
    z.append(a[b])
    s.append(b)
print(z)
#-----------------------------------------------5.15-------------------------------------------------------------


#-----------------------------------------------5.16-------------------------------------------------------------
# 5.16
import ctypes                                      # provides low-level arrays

class DynamicArray:
  """A dynamic array class akin to a simplified Python list."""

  def __init__(self):
    """Create an empty array."""
    self._n = 0                                    # count actual elements
    self._capacity = 1                             # default array capacity
    self._A = self._make_array(self._capacity)     # low-level array
    
  def __len__(self):
    """Return number of elements stored in the array."""
    return self._n
    
  def __getitem__(self, k):
    """Return element at index k."""
    if not 0 <= k < self._n:
      raise IndexError('invalid index')
    return self._A[k]                              # retrieve from array
  
  def append(self, obj):
    """Add object to end of the array."""
    if self._n == self._capacity:                  # not enough room
      self._resize(2 * self._capacity)             # so double capacity
    self._A[self._n] = obj
    self._n += 1

  def _resize(self, c):                            # nonpublic utitity
    """Resize internal array to capacity c."""
    B = self._make_array(c)                        # new (bigger) array
    for k in range(self._n):                       # for each existing value
      B[k] = self._A[k]
    self._A = B                                    # use the bigger array
    self._capacity = c

  def _make_array(self, c):                        # nonpublic utitity
     """Return new array with capacity c."""   
     return (c * ctypes.py_object)()               # see ctypes documentation

  def insert(self, k, value):
    """Insert value at index k, shifting subsequent values rightward."""
    # (for simplicity, we assume 0 <= k <= n in this verion)
    if self._n == self._capacity:                  # not enough room
      self._resize(2 * self._capacity)             # so double capacity
    for j in range(self._n, k, -1):                # shift rightmost first
      self._A[j] = self._A[j-1]
    self._A[k] = value                             # store newest element
    self._n += 1

  def remove(self, value):
    """Remove first occurrence of value (or raise ValueError)."""
    # note: we do not consider shrinking the dynamic array in this version
    for k in range(self._n):
      if self._A[k] == value:              # found a match!
        for j in range(k, self._n - 1):    # shift others to fill gap
          self._A[j] = self._A[j+1]
        self._A[self._n - 1] = None        # help garbage collection
        self._n -= 1                       # we have one less item
        return                             # exit immediately
    raise ValueError('value not found')    # only reached if no match
    
  def pop(self):
      # pop last element and resize array if capacity at 4 times what array holds
      obj = self._A[self._n-1]
      
      self._A[self._n]= None
      self._n -= 1
      if (self._n < self._capacity / 4):
          print('Resizing array to size ', self._capacity//2)
          self._resize(self._capacity//2)
      return obj
  
if __name__ == '__main__':
    da=DynamicArray() 
    for k in range(100):
        da.append(k)
    print(len(da), sys.getsizeof(da))
    for j in range(80):
        print(da.pop())
    print(len(da), sys.getsizeof(da))
    
    
    
#-----------------------------------------------5.17-------------------------------------------------------------
import ctypes                                      # provides low-level arrays
import time

class DynamicArray:
  """A dynamic array class akin to a simplified Python list."""

  def __init__(self):
    """Create an empty array."""
    self._n = 0                                    # count actual elements
    self._capacity = 1                             # default array capacity
    self._A = self._make_array(self._capacity)     # low-level array
    
  def __len__(self):
    """Return number of elements stored in the array."""
    return self._n
    
  def __getitem__(self, k):
    """Return element at index k."""
    if not 0 <= k < self._n:
      raise IndexError('invalid index')
    return self._A[k]                              # retrieve from array
  
  def append(self, obj):
    """Add object to end of the array."""
    if self._n == self._capacity:                  # not enough room
      self._resize(2 * self._capacity)             # so double capacity
    self._A[self._n] = obj
    self._n += 1

  def _resize(self, c):                            # nonpublic utitity
    """Resize internal array to capacity c."""
    B = self._make_array(c)                        # new (bigger) array
    for k in range(self._n):                       # for each existing value
      B[k] = self._A[k]
    self._A = B                                    # use the bigger array
    self._capacity = c

  def _make_array(self, c):                        # nonpublic utitity
     """Return new array with capacity c."""   
     return (c * ctypes.py_object)()               # see ctypes documentation

  def insert(self, k, value):
    """Insert value at index k, shifting subsequent values rightward."""
    # (for simplicity, we assume 0 <= k <= n in this verion)
    if self._n == self._capacity:                  # not enough room
      self._resize(2 * self._capacity)             # so double capacity
    for j in range(self._n, k, -1):                # shift rightmost first
      self._A[j] = self._A[j-1]
    self._A[k] = value                             # store newest element
    self._n += 1

  def remove(self, value):
    """Remove first occurrence of value (or raise ValueError)."""
    # note: we do not consider shrinking the dynamic array in this version
    for k in range(self._n):
      if self._A[k] == value:              # found a match!
        for j in range(k, self._n - 1):    # shift others to fill gap
          self._A[j] = self._A[j+1]
        self._A[self._n - 1] = None        # help garbage collection
        self._n -= 1                       # we have one less item
        return                             # exit immediately
    raise ValueError('value not found')    # only reached if no match
    
  def pop(self):
      # pop last element and resize array if capacity at 4 times what array holds
      obj = self._A[self._n-1]
      
      self._A[self._n]= None
      self._n -= 1
      if (self._n < self._capacity / 4):
          print('Resizing array to size ', self._capacity//2)
          self._resize(self._capacity//2)
      return obj
  
  def run_test(self, n):
      data = []
      for i in range(0, n):
          data.append(None)
      for i in range(0, n):
          data.pop()


if __name__ == '__main__':
    a = DynamicArray()
    for n in [10, 100, 1000, 10000, 100000, 1000000, 10000000]:
        start = time.time()
        a.run_test(n)
        end = time.time()
        print(n, end - start)
    


#-----------------------------------------------5.21-------------------------------------------------------------
#-5.21-
import time

# --4 ways to compose a long string

# 1. repeated concatenation
def string_append(string):
    s = ''
    for char in string:
        s += char
    return s
# 2. Append to temp list and then join 
def list_then_join(string):
    S = []
    for char in string:
        S.append(char)
    
    return ''.join(S)
# 3. list comprehension and then join 
def list_comp_join(string):
    return ''.join([x for x in string])
# 2. Generator comprehension then join 
def gen_comp_join(string):
    return ''.join(x for x in string)


for x in range(8):
    n = 10**x
    string = 'a'*n
    print()
    print ('x = ', x)
    start1 = time.time()
    string_append(string)
    end1 = time.time()
    print('String append', end1 - start1)
    
    start2 = time.time()
    list_then_join(string)
    end2 = time.time()
    print('list then join', end2 - start2)

    start3 = time.time()
    list_comp_join(string)
    end3 = time.time()
    print('List comp join', end3 - start3)
    
    start4 = time.time()
    gen_comp_join(string)
    end4 = time.time()
    print('Gen Comp join', end4 - start4)
    print()


#-----------------------------------------------5.22-------------------------------------------------------------
import time
import matplotlib as plt
# 1. Append to temp list and then join 
def list_append_join(string):
    S = []
    for char in string:
        S.append(char)
# 2. Extend temp list and then join 
def list_extend_join(string):
    S = []
    S.extend(string)
    #for char in string:
    #    S.extend(char)     

names = ['Append', 'Extend']
results = [[] for i in range(2)]
for x in range(9):
    n = 10**x
    string = 'a'*n
    print()
    print ('x = ', x)
    start1 = time.time()
    list_append_join(string)
    end1 = time.time()
    print('List append', end1 - start1)
    results[0].append(end1 - start1)
    
    start2 = time.time()
    list_extend_join(string)
    end2 = time.time()
    print('list extend', end2 - start2)
    results[1].append(end2 - start2)
    
    #below does not work very well
    x = []
    for i in range(9):
        x.append(10**i)
        
for i in range(len(results)):
    plt.pyplot.plot(x, results[i], label=names)
    plt.pyplot.legend()
    plt.pyplot.show()
    
    
#-----------------------------------------------5.23-------------------------------------------------------------
# 5.23
# p 207 expts show that list comprehension is significantly faster than building list by appending
# list comprehension
def list_compre(n):
    squares = [k*k for k in range(1,n+1)]
    return squares
# list append
def list_append(n):
    squares = []
    for k in range(1,n+1):
        squares.append(k*k)
    return squares

for x in range(7,10,1):
    n = 10**x
    print(n)
    start1 = time.time()
    list_compre(n)
    end1 = time.time()
    print('List comprehension', end1 - start1)
    
    start2 = time.time()
    list_append(n)
    end2 = time.time()
    print('list append', end2 - start2)
#-----------------------------------------------5.24-------------------------------------------------------------
#5.24
def remove(n, m, location):
    # n elements in list
    # m elements to remove
    # create data list
    S = []
    S = [k for k in range(1, n+1)] #make list 4 times as long
    mid = (m+1)//2
    if location == 'front':
        a, b, c = 1, m, 1
    if location == 'middle':
        a, b, c = mid, mid+m, 1
    if location == 'end':
        a, b, c = n, n+1-m, -1
    for i in range(a,b,c):
        S.remove(i)


if __name__ == '__main__':
    location = ['front', 'middle', 'end']
    nums = [1000, 10000, 100000]
    
    for k in (nums):
        for l in location:
            #print(l, k, 'removal')
            start1 = time.time()
            remove(k, k//3, l)
            
            end1 = time.time()
            print(l, k, 'removal', end1 - start1)
            
#-----------------------------------------------5.25-------------------------------------------------------------

lstCopy = [1,2,3,4,5,6,7,8,9,10,1,2,3,4,5,6,7,8,9,10,1,2,3,4,5,6,7,8,9,10]
print(lstCopy)
E = 10
while E in lstCopy: lstCopy.remove(E)
print(lstCopy)

#-----------------------------------------------5.26-------------------------------------------------------------

#5.26
# this is O(n)
S = list(range(100))
#Insert the repeats
for index, value in [(4,36), (83, 80), (20, 56), (54, 32), (10, 21)]:
    S[index] = value
    
prev_nums = set()
repeats = []
for i in S:
    if i in prev_nums:
        repeats.append(i)
    else:
        prev_nums.add(i)
print(repeats)

#-----------------------------------------------5.27-------------------------------------------------------------
# 5.27
import math
import random

def find_missing(S):
    max_num = 2**(math.ceil(math.log(len(S), 2))+1)
    num_count = [0]*(max_num+1)  # Create num count array
    for element in S:            # count the items
        num_count[element] += 1
        
    # we created a zero value array and updated counts, anything missing added here
    missing_nums = []            
    for i in range(len(num_count)):
        if num_count[i] == 0:
            missing_nums.append(i)
            
    return missing_nums
    

n = 20
S = [random.randint(0, 2**(math.ceil(math.log(len(S), 2))+1)-1) for _ in range(n)]
print(S)
print(find_missing(S))
#-----------------------------------------------5.28-------------------------------------------------------------
# 5.28
# Going thro loop of S elements once
#-----------------------------------------------5.29-------------------------------------------------------------
def create_join(A, B):
    # BOth A and B should be list 
    C = []
    for i in range(0,len(A)):
        for j in range(0, len(B)):
            
            if A[i][1] == B[j][0]:
                print('i', i, 'j', j,  'A[i][1]', A[i][1], 'B[j][0]', B[j][0])
                m = (A[i][0], A[i][1], B[j][1])
                C.append(m)
    return C

if __name__ == '__main__':
    A = [(1,1),(1,3), (3,4), (3,5), (5,6), (4,5)]
    B = [(1,4), (1, 5), (4, 2), (5, 1)]
create_join(A,B)
#-----------------------------------------------5.30-------------------------------------------------------------
import random

def insertion_sort_bk(A):
    """ Sort list of comparable elements into non decreasing order """
    for k in range(1, len(A)):
        cur = A[k]
        j = k
        while j > 0 and A[j-1] > cur:
            A[j] = A[j-1]
            j-=1
        A[j] = cur

def insertion_sort(S, current_position):
    i = current_position
    while i>0 and S[i]<S[i-1]: #Note, this will short circuit at i = 0 so you will never check S[0-1]
        S[i], S[i-1] = S[i-1], S[i]
        i -= 1
        
def packet_reciever_2(S):
    final_array = [None]*len(S)
    
    for i in range (len(S)):
        final_array[i] = S[i]
        insertion_sort(final_array, i)
        print(f'New Packet: {S[i]} ->', '\t', final_array)
    
     
S = list(range(17))
print(S)
random.shuffle(S)
print(S)
print('\n\nApproach 2 - Insertion Sort')        
packet_reciever_2(S)            

Q = list(range(17))
print(Q)
random.shuffle(Q)
print(Q)
insertion_sort_bk(Q)
print(Q)

#-----------------------------------------------5.31-------------------------------------------------------------

def list_r(S):
    total = 0
    if not isinstance(S, list):
        return S
    else:
        for element in S: total+= list_r(element)
    return total

def sum_list(S):
    total = list_r(S)
    return total

l = [[1,1,1,1,1], [2,2], 5]
sum_list(l)

#-----------------------------------------------5.32-------------------------------------------------------------


#-----------------------------------------------5.33-------------------------------------------------------------

def matmult(a,b):
    zip_b = zip(*b)
    # uncomment next line if python 3 : 
    # zip_b = list(zip_b)
    return [[sum(ele_a*ele_b for ele_a, ele_b in zip(row_a, col_b)) 
             for col_b in zip_b] for row_a in a]

x = [[1,2,3],[4,5,6],[7,8,9],[10,11,12]]
y = [[1,2],[1,2],[3,4]]

import numpy as np # I want to check my solution with numpy

mx = np.matrix(x)
my = np.matrix(y)     
matmult(x,y)
mx * my

