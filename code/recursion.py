# -*- coding: utf-8 -*-
"""
Created on Tue Sep  7 13:02:11 2021


"""

#-----------------------------------------------4.1-------------------------------------------------------------
import matplotlib.pyplot as plt
import numpy as np
import math

x = [i for i in range(2,20)]

funcs = [lambda x: 8*x,
         lambda x: 4*x*math.log(x),
         lambda x: 2*x**2,
         lambda x: x**3,
         lambda x: 2**x,]
ys = []
for func in funcs:
    ys.append(list(map(func, x)))

for y in ys:
    plt.plot(x, y)
plt.yscale('log')
plt.xscale('log')
    
#-----------------------------------------------4.2-------------------------------------------------------------
def power(x, n):
    
    """
    
    Parameters
    ----------
    x : int
        number whose power will be computed
    n : int
        exponent
    Returns
    -------
    x^n
    
    """
    if n == 0:
        return 1
    else:
        return x * power(x, n-1)
    

#-----------------------------------------------4.6-------------------------------------------------------------
# 4.6
def HarmonicNumber(n):
    """ Find nth harmonic number """
    if n < 1:
        print("invalid num:  num should be positive int greater than 0")
    if n == 1:
        return 1
    else:
        return 1/n + HarmonicNumber(n-1)

HarmonicNumber(3)
    
#-----------------------------------------------4.7-------------------------------------------------------------
# 4.7
def ConvertStringToInt(S, n):
    if n < 0:
        print("invalid n - should be between 1 and len(S)")
    print(len(S)-n, S[len(S)-n])
    num = ConvertChrToInt(S[len(S)-n])
    if num < 0 or num > 9:
        print('invalid chr')
    if n == 1:  # base case
        return num
#    print('calc',num,n, n-1, 10**(n-1), 10**(n-1) * num)
    return 10**(n-1) * num + ConvertStringToInt(S, n-1)

def ConvertChrToInt(S):
    num = 0
    num = ord(S)-ord('0')
    if num < 0 or num > 9:
        print('invalid chr')
        return
    else:
        return num
    
    

#-----------------------------------------------4.9-------------------------------------------------------------
def FindMinMax(S, n=0):
    """ find min and max in sequence S"""
    if n == len(S) - 1: 
        return (S[n], S[n])
    else:
        min_val, max_val = FindMinMax(S, n+1)
        return min(min_val, S[n]), max(max_val, S[n])

def FindMinMax2(S, n):
    """ find min and max in sequence S"""
    if n is None:
        n = len(S) - 1
    if n == 0: 
        return (S[n], S[n])
    else:
        min_val, max_val = FindMinMax2(S, n-1)
        return min(min_val, S[n]), max(max_val, S[n])

  
    
print(FindMinMax([1,2,3,4,5,6,7,8]))
print(FindMinMax([-45,2,774,5,6,7,8]))
print(FindMinMax([8,7,6,5,4,3,2,1]))    
    
print(FindMinMax2([1,2,3,4,5,6,7,8], None))
print(FindMinMax2([-45,2,774,5,6,7,8], None))
print(FindMinMax2([8,7,6,5,4,3,2,1], None))    
    
#-----------------------------------------------4.10-------------------------------------------------------------
def ComputeIntLogOfBaseTwo(n, base):
    """ n - number whose base 2 log needs to be computed"""
    # divide by 2, keep track of number of divisions until value less than or equal to 1
    # log 100 base 10 = 2  --> 100/10 = 10, 10/10 = 1
    # log 8 base 2 = 3  --> 8/2 = 4 (div 1), 4/2 = 2 (div 2), 2/2 = 1 (div 3) Ans: 3
    
    #check n and base are integers
    if (type(n) != int and type(n) != float) or type(base) != int:
        print('Not valid - n must be int or float and base must be int')
        return
    # base case
    if n/base >= 1:
        return 1 + ComputeIntLogOfBaseTwo(n/base, base)
    else:
        return 0

print(ComputeIntLogOfBaseTwo(8,2))
#-----------------------------------------------4.11-------------------------------------------------------------
def UniqueNSquared(S, n1=None, n2=None):
    """ Determine if list is unique by using 2 for loops - but using recursion instead """
    S_len = len(S)
    if n1 is None:
        n1 = S_len - 1
    if n2 is None:
        n2 = S_len - 1
    if n1 == 0 and n2 == 0:
        print(n1, n2, S[n1], S[n2])
        return True  #Base case one element and is unique
    if S[n1] == S[n2] and (n1 != n2):
        print(n1, n2, S[n1], S[n2])
        return False
    else:
        if n2 == 0:
            return UniqueNSquared(S, n1 - 1, S_len - 1)
        else:
            return UniqueNSquared(S, n1, n2 - 1)
    return

print(UniqueNSquared([1,2,3,5,6,8,8], None, None))
print(UniqueNSquared([1,2,3,5,6,8], None, None))

#-----------------------------------------------4.12-------------------------------------------------------------
def ComputeProduct(m,n):
    """ 2*3 = 2+2+2 """
    # we could switch the largest parameter the first time
    if type(m) != int or type(n) != int or m < 0 or n < 0:
        print('Not valid - both m and n must be positive integers')
        return
    if n == 0:
        return 0
    else:
        return m + ComputeProduct(m,n-1)

#-----------------------------------------------4.14-------------------------------------------------------------
def printmove(fr, to):
    print('move from ' + str(fr) + ' to ' + str(to))
    
def TowersOfHanoi(n, frPeg, toPeg, sparePeg):
    """ 
    n - number of disks
    a,b,c - three pegs
    a has all disks - largest disks at bottom
    c disks need to be transferred to c peg without any larger being on top of smaller
    b temp storage
    """
    if n == 1:
        printmove(frPeg, toPeg)
    else:
        TowersOfHanoi(n-1, frPeg, sparePeg, toPeg)
        TowersOfHanoi(1, frPeg, toPeg, sparePeg)
        TowersOfHanoi(n-1, sparePeg, toPeg, frPeg)

    
#-----------------------------------------------4.15-------------------------------------------------------------
def SubSets(S, n=None, n1=None, n1_1=None):
    """ 
    S  - Set from which to get subsets
    n  - num of elements in subset
    n1 - num of elements in subset
    n1_1 - current element
    """
    if n is None or n1 is None or n1_1 is None:
        n = len(S)
        n1 = 0
        n1_1 = 0
    if n =- len(S):
        A = set()
    if n == 0:
        A.add(())
    else:
        print() 
    return

#-----------------------------------------------4.16-------------------------------------------------------------
def Reverse(S, n=0):
    """ reverse string S"""

    print(n, n+1, n/2, S, n + 1 < len(S) /2)

    if n == len(S) - 1:
        return [S[n]]
    else:
        result = Reverse(S, n+1)
        result.append(S[n])
        if n == 0:
            result = ''.join(result)
        return result
    
#-----------------------------------------------4.17-------------------------------------------------------------
def IsPalindrome(S, n=0):
    len_S = len(S)
    if len_S == 1:
        print(1)
        return True
    if n >= len_S//2 :
        print(2)
        return S[n] == S[len_S//2]
    else:
        print(3)
        return (S[n] == S[len_S-n - 1] and IsPalindrome(S, n+1))


#-----------------------------------------------4.18-------------------------------------------------------------


def MoreVowels(S, n=0):
    a = 1 if S[n] in 'aeiou' else -1
    if n == len(S) - 1:
        return a
    else:
        return a + MoreVowels(S, n+1) 

#-----------------------------------------------4.19-------------------------------------------------------------
def EvenBeforeOdd(S, n=0):
    #base case
    if n == len(S) - 1:
        return [S[n]]
    #other case
    else:
        if S[n] % 2 == 1: #odd - add to end of list
            return EvenBeforeOdd(S, n+1) + [S[n]]
        else:
            return [S[n]]+ EvenBeforeOdd(S, n+1) 
        
S = [[1,2,3,4,5,6,7,8], [4,3,65,23,5,46,765,3,45,23], [1], [2,2]]
for seq in S:
    print(EvenBeforeOdd(seq)   )
#-----------------------------------------------4.20-------------------------------------------------------------
def AboveBelowK(S, k, n=0):
    if len(S)==1:
        return S 
        
    elif n == len(S)-1:    #last index
        if S[n] < k:   # lower than k
            return [S[n]], [], []
        elif S[n] > k:    # higher than k
            return [], [], [S[n]]
        else:  # equals k
            return [], [S[n]], []  #Should return k in the middle list
        
    else:
        below, at, above = AboveBelowK(S, k, n+1)
        if S[n] < k:   # lower than k
            below = add_lists(below, [S[n]])
        elif S[n] > k:   # above than k
            above = add_lists(above, [S[n]])
        else:    # at k
            at = add_lists(at, [S[n]])
            
        if n == 0:
            return add_lists(below, add_lists(at, above)) 
        else:
            return below, at, above

def add_lists(a,b): #There are issues adding a [a] + [], so this circumvents the problem
    if a and b:
        return a+b
    else:
        return b or a #if one of them is [], return the other
    
seq = [11,2,33,4,5,6,7,8,9,10]
AboveBelowK(seq, 8)
# running time O(n)



#-----------------------------------------------4.21-------------------------------------------------------------
# due to the use of dictionary this is running at O(n) and not O(n^2) via brute force method
def SummingInts(S, target_val, keyset = None, n=0):
    if keyset is None:
        keyset = set()
    
    if len(S) <= 1:  # nothing possible in zero or one element set
        return None
    reqd_val = target_val - S[n]
    
    if n == len(S) - 1: # at last element - either we have a match (return set) or not (return None)
        if reqd_val in keyset: 
            return (reqd_val, S[n])
        else: 
            return None
    else:
        if reqd_val in keyset:
            return (reqd_val, S[n])
        else:
            keyset.add(S[n])
            return SummingInts(S, target_val, keyset, n+1)
        
        
seq = [11,2,33,4,5,6,7,8,9,10,1]         
tgt = 10
SummingInts(seq, tgt)

#-----------------------------------------------4.22-------------------------------------------------------------

def powwow(x, n):
    """ compute non-recursive power w/o using pow function and using repeated squaring"""
    if n == 0:
        return 1
    
    retVal = x
    i = 1
    while i*2 <= n:
        print(i, i*2, 'start', retVal)
        retVal *= retVal 
        print(i, i*2, 'endval', retVal)
        i *= 2
        
    remain = n - i
    while remain > 0:
        retVal *= x
        print(remain,  'endval2', retVal)
        remain -= 1
        
    return retVal

powwow(2, 4)
powwow(2, 5)
powwow(2, 14)
powwow(5, 13)        
#-----------------------------------------------4.23-------------------------------------------------------------

import os

def FindFiles(path, findfilename):
    """ Return matching files in file/folder and descendants """
    
    if os.path.isdir(path):
        for obj in os.listdir(path):
            if os.path.isdir(os.path.join(path, obj)):
                FindFiles(os.path.join(path, obj), findfilename)
            elif obj == findfilename:
                print(os.path.join(path, obj))
            


FindFiles('C:\\junk', 'meow.txt')


#-----------------------------------------------4.25-------------------------------------------------------------


"""
The hint is that we should use a loop from 0 to 2**c -2
and that the number of ticks should be one more than the number of consecutive 1s.

"""

def english_ruler(n = 3, repeats = 10):
    limit = repeats*(2**n -2)
    counter = 0
    while counter<=limit:
        dashes = 1
        sub_counter = counter 
        while sub_counter & 1:
            dashes += 1
            sub_counter = sub_counter >> 1
        dashes = min (dashes, n)
        print('-'*dashes)
        counter += 1
        
        
english_ruler(4, 3)
#-----------------------------------------------4.26-------------------------------------------------------------

def printmove(fr, to):
    print('move from ' + str(fr) + ' to ' + str(to))
    
def TowersOfHanoi(n, frPeg, toPeg, sparePeg):
    """ 
    n - number of disks
    a,b,c - three pegs
    a has all disks - largest disks at bottom
    c disks need to be transferred to c peg without any larger being on top of smaller
    b temp storage
    """
    if n == 1:
        printmove(frPeg, toPeg)
    else:
        TowersOfHanoi(n-1, frPeg, sparePeg, toPeg)
        TowersOfHanoi(1, frPeg, toPeg, sparePeg)
        TowersOfHanoi(n-1, sparePeg, toPeg, frPeg)
        
#-----------------------------------------------4.27-------------------------------------------------------------

for obj in os.walk('c:\\junk'):
    print(obj)



import os

def Dirlisting(path):
    """ files in directory """
    
    if os.path.isdir(path):
        for obj in os.listdir(path):
            if os.path.isdir(os.path.join(path, obj)):
                Dirlisting(os.path.join(path, obj))
            else:
                print(os.path.join(path, obj))
            

Dirlisting('C://junk')

import os

def our_walk(path):
    folders = []
    files = []
    
    for obj in os.listdir(path):
        new_path = os.path.join(path, obj)
        if os.path.isdir(new_path):
            folders.append(obj)
            yield from our_walk (new_path)  #Note the use of yield from
        elif os.path.isfile(new_path):
            files.append(obj)
        else:
            print('Unknown object:', obj)
    
    yield(path, folders, files)

for i in os.walk('C:\\junk'):
    print(i)

for i in our_walk('C:\\junk'):
    print(i)
    