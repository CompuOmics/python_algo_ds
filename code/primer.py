# -*- coding: utf-8 -*-
"""
Created on Tue Aug 24 12:15:24 2021

@author: 
"""

# R-1.1

def is_multiple(n,m):
    return n % m == 0

is_multiple(10,2)
is_multiple(11,2)

# R-1.2
def is_even(k):
    return not(k & 1 )

#QB logic
# ALL EVEN Numbers end with bit 0
# 0 & 1 is 0 which is false

is_even(100)
is_even(1001)


# R-1.3
def minmax(data):
    if len(data) == 0:
        return
    min, max = data[0], data[0]
    for x in data:
        if (min > x):
            min = x
        if (max < x):
            max = x
    return (min, max)

data = [1,2,3,4,5,6,7]
minmax(data)

# R-1.4
def squaresum(k):
    if k < 0 :
        return
    return sum(i**2 for i in range(k))
    
squaresum(4)

# R-1.5
def squaresum(k):
    if k < 0 :
        return
    return sum(i**2 for i in range(k))

squaresum(40)

# R-1.6
def squareoddsum(k):
    if k < 0 :
        return
    return sum(i**2 for i in range(k) if i%2 == 1)

squareoddsum(5)
# 0,1,2,3,4 --> 1**2 +3**2


# R-1.7
def squareoddsum(k):
    if k < 0 :
        return
    return sum(i**2 for i in range(k) if i%2 == 1)

squareoddsum(5)
# 0,1,2,3,4 --> 1**2 +3**2

# R-1.8
s = "mystring"
k = -3
l = len(s)
s[k]
s[len(s) + k]

# R-1.9
range(50,90,10)
list(range(50,90,10))

# R-1.10
list(range(8,-10,-2))

# R-1.11
k = 9
list(2**i for i in range(k))

# R-1.12
import random
data = [1,2,3,4,5,6,7,8,9,10]
print(random.choice(data))

def myChoice(data):
    return data[random.randrange(len(data))]

data= [x for x in range(5,12,1)]
random.choice(data)

myChoice(data)


#----------------------------------------------------------------
#   Creativity
#----------------------------------------------------------------
# C-1.13
mylist = [1,2,3,4,5,6,7,8,9,10]
print(mylist)
mylist.reverse()
print(mylist)

def myreverse(data):
    return data[::-1]

mylist = [1,2,3,4,5,6,7,8,9,10]
print(mylist)
print(list(myreverse(mylist)))


# C-1.14
def oddProduct(data):
    l = len(data)
    return [(data[i], data[j],data[i]*data[j]) for i in range(l) 
            for j in range(l) if (data[i]*data[j])%2 == 1 and  data[i] != data[j] and i < j]
    

mylist = [1,2,3,4,5,6,7,8,9,10]
print(oddProduct(mylist)    )

def oddPairLC(s):
    l=len(s)
    op=[(s[i],s[j],s[i]*s[j])  for i in range(l) for j in range(i) if (s[i]*s[j])%2 == 1 and  s[i] != s[j] ]
    return op

def DistinctEfficientPair(s):
    l=len(s)
    op=[(s[i],s[j])  for i in range(l) for j in range(i) if s[i] != s[j] ]
    return op

print(DistinctEfficientPair(mylist))

# C-1.15
def distinctData(data):
    dataset = set(data)
    return len(dataset) == len(data)
        
                
mylist = [1,2,3,4,5,6,7,8,9,10]
print(distinctData(mylist))
myredundantlist = [1,2,3,4,5,6,7,8,9,10,10,9,8]
print(distinctData(myredundantlist))



# C-1.16
def scale(data, factor):
    for j in range(len(data)):
        data[j] *= factor
        
def test():
    data = [1,2,3,4,5]
    print(data)
    scale(data, 6)
    print(data)

test()    

# C-1.17

# C-1.18
k = 10
l =(i*(i+1) for i in range(k) )
print(list(l))

# C-1.19
i = ord('a')
j = ord('z')
print([ chr(k) for k in range(i,j+1,1)])

# C-1.20
import random as r
mydata = [1,2,3,4,5,6,7,8,9,10]
print(mydata)
r.shuffle(mydata)
print(mydata)

r.randint(1,10)

def swapItem(s,i,j):
    s[i],s[j]=s[j],s[i]
    return

mydata = [1,2,3,4,5,6,7,8,9,10]
def myshuffle(mydata):
    l = len(mydata)
    for i in range(l):
        k = r.randint(i, l-1)
        swapItem(mydata, i, k)

s=list(range(5))

swapItem(mydata, 3,2)
print(mydata)    
    
myshuffle(mydata)
print(mydata)

# C-1.21
def readAndReverseInput():
 
    myInput = []
    try:
        while True:
            myInput.append( str(input('next line: ')))
    except EOFError:
        False
    myInput.reverse()
    print(myInput)
        
readAndReverseInput()
        
# C-1.22
a = [1,2,3,4,5]
b = [6,7,8,9,10]

def arrProduct(a, b):
    if len(a) != len (b):
        return
    return[ai * bi for ai,bi in zip(a, b)]

arrProduct(a, b)

# C-1.23
def CatchingIndexError(b, i):
    try:
        print(b[i])
    except IndexError:
        print('Dont try buffer overflow attacks in python')
    
CatchingIndexError(a, 4)
CatchingIndexError(a, 9)

# C-1.24
def vowelCount(data, vowels):
    print(data)
    print(vowels)
    return sum([1 for k in data if k.lower() in vowels.lower()])

data = "hi how is the weather today"
vowels = 'aeiou'
vowelCount(data, vowels)
# C-1.25
def removeCharacters(data, charsToRemove):
    return ''.join([k for k in data if k.lower() not in charsToRemove.lower()])

data = "hi! how is the #$%^ weather today?"
charsToRemove = ',!;:?#$%^'
removeCharacters(data, charsToRemove)
# C-1.26

def validMathOperations(a,b,c):
    if (a + b == c):
        print('a + b = c can add a and b to get c')
    elif (a - b == c ):
        print('a - b = c can subtract b from a to get c')
    elif(a * b == c):
        print('a * b = c can multiply a and b to get c')
    elif(a / b == c):
        print('a / b = c can divide a by b to get c')        
    else:
        print("Invalid numbers")

validMathOperations(12, 4, 16)
validMathOperations(16, 2, 8)
validMathOperations(17, 2, 15)
validMathOperations(3, 7, 21)
validMathOperations(17, 5, 19)


# C-1.27
def factors(n):
    myfactors = []
    k = 1
    while k * k < n:
        if n % k == 0:
            myfactors.append(n // k)
            yield k
        k += 1
    if k * k == n:
        yield k
    myfactors.reverse()
    for factor in myfactors:
        yield factor

list(factors(16) )

# C-1.28
def pNorm(mydata, p):
    return sum(k**p for k in mydata) ** (1/p)

pNorm([4,3],2)
pNorm([4,3],3)

# P-1.29
from itertools import permutations as perm 

def allPermutations(data):
    allPerms = perm(data)
    for myPerm in list(allPerms):
        print(myPerm)
        
allPermutations('catdog')

#-----------------------
#==Chp1: P-1.29============
def getAPerm(s):
    from itertools import permutations as perm 
    l= len(s)
    p=[]
    for i in range(1,l+1):
        for t in list(perm(s,i)): #perm-length i
            p.append("".join(t))
    return p
getAPerm("cat")
#Out[38]: 
#['c',
# 'a',
# 't',
# 'ca',
# 'ct',
# 'ac',
# 'at',
# 'tc',
# 'ta',
# 'cat',
# 'cta',
# 'act',
# 'atc',
# 'tca',
# 'tac']
len(getAPerm("catdog"))
#Out[39]: 1956
#-----------------------

# C-1.30
def p130(num):
    if not isinstance(num, int) or num <= 2:
        print("number should be an integer greater than 2")
        return
    i = 0
    k = num
    while k/2 >= 2:
        i += 1
        k = k/2
    return i

p130(120)    
p130(12)
# 12 --> 6, 3
p130(5)
p130(3)    
p130(1)    
p130(2)    
    
p130('hello')    
    
# C-1.31
# C-1.32
# C-1.33

# C-1.34
def punishmentAlgo(sentence, multiple):
    # need 8 typos
    t = []
    for i in range(8):
        t.append(random.randint(0 , multiple))
        
    for i in range(multiple):
        if (i in t):
            # position to switch
            k = random.randint(0 , len(sentence))
            randletter = chr(random.randint(ord('a'), ord('z')))
            print(sentence[:k-1] + randletter + sentence[k+1:])
        else:
            print(sentence)
        
        


punishmentAlgo("It is going to be a beautiful day", 100)
    
    






