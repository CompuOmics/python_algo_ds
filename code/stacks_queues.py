# -*- coding: utf-8 -*-
"""
"""

#-----------------------------------------------6.1-------------------------------------------------------------
#  6.1

class Empty(Exception):
    """ Error raised when attempting to access an element from an empty container"""
    pass

class ArrayStack:
    """ LIFO Stack implementation using a Python list as underlying storage"""
    def __init__(self):
        """ Create an empty stack """
        self._data = []
        
    def __len__(self):
        """ Returns number of elements in stack """
        return len(self._data)
    
    def is_empty(self):
        """ Return True if the stack is empty """
        return len(self._data) == 0
        
    def push(self, e):
        """ Add element e to the top of the stack """
        self._data.append(e)
        
    def top(self):
        """ Return (but do not remove) element at top of stack. If empty - raise Exception"""
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data[-1]       # return last item in the list
        
    def pop(self):
        """ Remove and return element at top of stack. If empty - raise Exception"""
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data.pop()       # return last item in the list

if __name__ == '__main__':
    stk = ArrayStack()
    stk.push(5)         # 5
    stk.push(3)         # 5, 3
    print(stk.pop())    # 5         # pop 3   
    stk.push(2)         # 5, 2
    stk.push(8)         # 5, 2, 8
    print(stk.pop())    # 5, 2      # pop 8
    print(stk.pop())    # 5         # pop 2   
    stk.push(9)         # 5, 9
    stk.push(1)         # 5, 9, 1
    print(stk.pop())    # 5, 9      # pop 1
    stk.push(7)         # 5, 9, 7
    stk.push(6)         # 5, 9, 7, 6
    print(stk.pop())    # 5, 9, 7   # pop 6
    print(stk.pop())    # 5, 9      # pop 7
    stk.push(4)         # 5, 9, 4
    print(stk.pop())    # 5, 9,     # pop 4
    print(stk.pop())    # 5, 9      # pop 9

#-----------------------------------------------6.2-------------------------------------------------------------
#  6.2
# 25 - 10 + 3 = 18
#-----------------------------------------------6.3-------------------------------------------------------------
#  6.3
def transfer(S, T):
    for i in range(len(S)):
        T.push(S.pop()  )
        
S = ArrayStack()
S.push(1)
S.push(2)
S.push(3)
S.push(4)
S.push(5)
S.push(6)
S.push(7)
T = ArrayStack()
transfer(S, T)
for j in range(len(T)):
    print(T.pop())
    
    
    
#-----------------------------------------------6.4-------------------------------------------------------------
#  6.4
class Empty(Exception):
    """ Error raised when attempting to access an element from an empty container"""
    pass

class ArrayStack:
    """ LIFO Stack implementation using a Python list as underlying storage"""
    def __init__(self):
        """ Create an empty stack """
        self._data = []
        
    def __len__(self):
        """ Returns number of elements in stack """
        return len(self._data)
    
    def is_empty(self):
        """ Return True if the stack is empty """
        return len(self._data) == 0
        
    def push(self, e):
        """ Add element e to the top of the stack """
        self._data.append(e)
        
    def top(self):
        """ Return (but do not remove) element at top of stack. If empty - raise Exception"""
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data[-1]       # return last item in the list
        
    def pop(self):
        """ Remove and return element at top of stack. If empty - raise Exception"""
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data.pop()       # return last item in the list
    
    def _pop_all_recursive(self, results, counter):
        """ Remove and return all elements from stack. If empty - raise Exception"""
        if self.is_empty():
            return None
        else:
            results[counter] = self._data.pop()
            counter += 1
            self._pop_all_recursive(results, counter)
            
    def pop_all(self):
        """ Remove and return all elements from stack. """
        results = [None]*len(self._data)
        counter = 0
        self._pop_all_recursive(results, counter)
        return results
    
    def __str__(self):
        """Produce string representation of vector."""
        return str(self._data)  # adapt list representation

    
        
if __name__ == '__main__':
    stk = ArrayStack()
    stk.push(1)
    stk.push(2)
    stk.push(3)
    stk.push(4)
    print(stk.pop_all())
    # [4, 3, 2, 1]
    
#-----------------------------------------------6.5-------------------------------------------------------------
#  6.5
def problem6_5(S, T):
    """ S is list with elements - they are pushed to T 
        return list with elements in reverse order"""
    U = []
    for i in range(len(S)):
        T.push(S[i])
    for i in range(len(S)):
        U.append(T.pop())
    return U

S = [1,2,3,4,5]
T = ArrayStack()
U = problem6_5(S,T)
print(U)
        

#-----------------------------------------------6.7-------------------------------------------------------------
#  6.7


class Empty(Exception):
    """ Error raised when attempting to access an element from an empty container"""
    pass

class ArrayQueue:
    DEFAULT_CAPACITY = 10
    
    def __init__(self):
        self._data = [None]* ArrayQueue.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0
    
    def __len__(self):
        """ Return number of elements in the queue"""
        return self._size
    
    def is_empty(self):
        return self._size == 0
    
    def first(self):
        """ Return w/o removing first element of Q front"""
        if self.is_empty():
            raise Empty("Queue is empty")
        return self._data[self._front]
            
    def dequeue(self):
        """ Return and remove first element of Q front"""
        if self.is_empty():
            raise Empty("Queue is empty")
        answer = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        #if 0 < self._size < len(self._data) // 4:
        #    self._resize(  len(self._data) // 2)
        return answer
    
    def enqueue(self, e):
        """ Add an element to the back of the queue"""
        if self._size == len(self._data):
            self._resize(2 * len(self._data))
        queuing_pt = (self._front + self._size) % len(self._data)
        self._data[queuing_pt] = e
        self._size += 1
    
    def _resize(self, cap):
        """ resize to new list with new capacity """
        print('Resizing to new capacity', cap)
        olddata = self._data
        self._data = [None] * cap
        copy_position = self._front
        for i in range(self._size):
            self._data[i] = olddata[copy_position]
            copy_position = (copy_position + 1) % len(olddata)
        self._front = 0
        #print((self._front + self._size) % len(self._data))
        
    def __str__(self):
        """Produce string representation of vector."""
        return str(self._data)  # adapt list representation
        
if __name__ == '__main__':
    aq = ArrayQueue() 
    aq.enqueue(5)
    aq.enqueue(3)
    print(aq.dequeue())
    aq.enqueue(2)
    aq.enqueue(8)
    print(aq.dequeue())
    print(aq.dequeue())
    aq.enqueue(9)
    aq.enqueue(1)
    print(aq.dequeue())
    aq.enqueue(7)
    aq.enqueue(6)
    print(aq.dequeue())
    print(aq.dequeue())
    aq.enqueue(4)
    print(aq.dequeue())
    print(aq.dequeue())
    aq.enqueue(11)
    aq.enqueue(12)
    aq.enqueue(13)
    aq.enqueue(14)
    aq.enqueue(15)
    aq.enqueue(16)
    aq.enqueue(17)
    aq.enqueue(18)
    aq.enqueue(19)
    aq.enqueue(20)
    
    

#-----------------------------------------------6.11-------------------------------------------------------------
#  6.11
from collections import deque

class Empty(Exception):
    """ Error raised when attempting to access an element from an empty container"""
    pass

class ArrayDeQueQueue:
    DEFAULT_CAPACITY = 10
    
    def __init__(self):
        self._data = deque([])
        self._size = 0
    
    def __len__(self):
        """ Return number of elements in the queue"""
        return len(self._data)
    
    def is_empty(self):
        return len(self._data) == 0
    
    def first(self):
        return self._data[0]

    def dequeue(self):
        """ Return and remove first element of Q front"""
        if self.is_empty():
            raise Empty('Queue is empty')
        else:
            ans = self._data.popleft()
            self._size -= 1
            return ans
    
    def enqueue(self, e):
        """ Add an element to the back of the queue"""
        self._data.append(e)
        self._size += 1
    

        
if __name__ == '__main__':
    aq = ArrayDeQueQueue() 
    aq.enqueue(5)
    aq.enqueue(3)
    print(aq.first())
    print(aq.dequeue())
    aq.enqueue(10)
    print(aq.first())
    

#-----------------------------------------------6.12-------------------------------------------------------------
#  6.12
from collections import deque
de = deque()
de.appendleft(4)  # 4
de.append(8)      # 4, 8
de.append(9)      # 4, 8, 9
de.appendleft(5)  # 5, 4, 8, 9
print(de)         # 5, 4, 8, 9
print(de[len(de)-1])  # 9
print(de.popleft())# 4, 8, 9
print(de.pop())    # 4, 8
de.append(7)       # 4, 8, 7
print(de[0])       # 4
print(de[len(de)-1]) # 7
de.append(6)       # 4, 8, 7, 6
print(de.popleft()) # 8, 7, 6
print(de.popleft()) # 7, 6
print(de)           # 7, 6
#-----------------------------------------------6.13-------------------------------------------------------------
#  6.13
Q = ArrayQueue()
de = deque([1,2,3,4,5,6,7,8])
print(de)
Q.enqueue(de.popleft())
print(de)
Q.enqueue(de.popleft())
print(de)
Q.enqueue(de.popleft())
print(de)
de.append(de.popleft())
print(de)
Q.enqueue(de.popleft())
print(de)
de.appendleft(de.pop())   # 4,6,7,8
print(de)
de.append(Q.dequeue())
print(de)
de.append(Q.dequeue())
print(de)
de.append(Q.dequeue())
print(de)
de.appendleft(Q.dequeue())
print(de)
de.appendleft(de.pop())
print(de)
de.appendleft(de.pop())
print(de)
de.appendleft(de.pop())
print(de)

#-----------------------------------------------6.14-------------------------------------------------------------
#  6.14
S = ArrayStack()
de = deque([1,2,3,4,5,6,7,8])
print(de)
S.push(de.popleft())
print(de)
S.push(de.popleft())
print(de)
S.push(de.popleft())
print(de)
de.append(de.popleft())
print(de)
S.push(de.popleft())
print(de)
de.appendleft(de.pop())
print(de)
de.appendleft(S.pop())
print(de)     
de.appendleft(S.pop())              
print(de)
de.appendleft(S.pop())              
print(de)
de.appendleft(S.pop())              
print(de)
#-----------------------------------------------6.15-------------------------------------------------------------
#  6.15
import random
def max_prob(S, nums):
    random.shuffle(nums)
    for num in nums:
        #print(num)
        S.push(num)
    x = S.pop()
    return ( x if x > S.top() else S.pop() )



num_trials = 1000
total_trials = 0
numbers = [1,2,3]
S=ArrayStack()
for i in range(num_trials):
    result = max_prob(S, numbers)
    if result  == max(numbers):
        total_trials += 1
print(f'The probablity of picking correct max is: {total_trials/num_trials * 100}%')


#-----------------------------------------------6.16-------------------------------------------------------------
#  6.16
class Empty(Exception):
    """ Error raised when attempting to access an element from an empty container"""
    pass

class Full(Exception):
    """ Error raised when attempting to access an element from an empty container"""
    pass

class ArrayStack:
    """ LIFO Stack implementation using a Python list as underlying storage"""
    def __init__(self, cap=None):
        """ Create an empty stack """
        self._data = []
        if cap is None: cap = 10
        self._max_capacity = cap
        
    def __len__(self):
        """ Returns number of elements in stack """
        return len(self._data)
    
    def is_empty(self):
        """ Return True if the stack is empty """
        return len(self._data) == 0
        
    def push(self, e):
        """ Add element e to the top of the stack """
        if len(self._data) >= self._max_capacity:
            raise Full('Stack is full')
        self._data.append(e)
        
    def top(self):
        """ Return (but do not remove) element at top of stack. If empty - raise Exception"""
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data[-1]       # return last item in the list
        
    def pop(self):
        """ Remove and return element at top of stack. If empty - raise Exception"""
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data.pop()       # return last item in the list
    
    def _pop_all_recursive(self, results, counter):
        """ Remove and return all elements from stack. If empty - raise Exception"""
        if self.is_empty():
            return None
        else:
            results[counter] = self._data.pop()
            counter += 1
            self._pop_all_recursive(results, counter)
            
    def pop_all(self):
        """ Remove and return all elements from stack. """
        results = [None]*len(self._data)
        counter = 0
        self._pop_all_recursive(results, counter)
        return results

    def __str__(self):
        """Produce string representation of vector."""
        return str(self._data)  # adapt list representation

if __name__ == '__main__':
    stk = ArrayStack(5)
    stk.push(1)
    stk.push(2)
    stk.push(3)
    stk.push(4)
    stk.push(5)
    stk.push(6)
    
    stk2 = ArrayStack()
    for i in range(12): 
        print(i)
        stk2.push(i)
    
#-----------------------------------------------6.17-------------------------------------------------------------
#  6.17
class Empty(Exception):
    """ Error raised when attempting to access an element from an empty container"""
    pass

class Full(Exception):
    """ Error raised when attempting to access an element from an empty container"""
    pass

class ArrayStackPreAllocated:
    """ LIFO Stack implementation using a Python list as underlying storage"""
    def __init__(self, cap=25):
        """ Create an empty stack """
        self._data = [None] * cap
        self._max_capacity = cap
        self._n = 0
        
    def __len__(self):
        """ Returns number of elements in stack """
        return self._n
    
    def is_empty(self):
        """ Return True if the stack is empty """
        return len(self._data) == 0
        
    def push(self, e):
        """ Add element e to the top of the stack """
        if self._n == self._max_capacity:
            raise Full('Stack is full')
        self._data[self._n] = e
        self._n += 1
        
    def top(self):
        """ Return (but do not remove) element at top of stack. If empty - raise Exception"""
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data[self._n-1]       # return last item in the list
        
    def pop(self):
        """ Remove and return element at top of stack. If empty - raise Exception"""
        if self.is_empty():
            raise Empty('Stack is empty')
        ans = self._data[self._n - 1]
        self._data[self._n - 1] = None
        self._n -= 1
        return self._data.pop()       # return last item in the list
    

        
if __name__ == '__main__':
    apstack = ArrayStackPreAllocated(10)

    for i in range(20):
        try:
            apstack.push(i)
            print(apstack.top())
        except Full as e:
            print(e)


#-----------------------------------------------6.18-------------------------------------------------------------
#  6.18
def transfer(S):
    s1 = ArrayStack()
    s2 = ArrayStack()
    for i in range(len(S)):
        s1.push(S.pop()  )
        
    for i in range(len(s1)):
        s2.push(s1.pop())
    
    for i in range(len(s2)):
        S.push(s2.pop())
        
S = ArrayStack()
for i in range(10):
    S.push(i)

transfer(S)
for j in range(len(S)):
    print(S.pop())

    
#-----------------------------------------------6.19-------------------------------------------------------------
#  6.19
def is_matched_html(raw):
    """Return True if all HTML tags are 
    properly matched False otherwise"""
    S = ArrayStack()
    j = raw.find('<')
    while j != -1:
        k = raw.find('>', j+1)
        sp = raw.find(' ', j+1)
        if k == -1:
            return False
        if (sp > 0  and sp < k):
            tag = raw[j+1:sp]
            
        else:
            tag = raw[j+1:k]
        print(tag)
        if not tag.startswith('/'):
            S.push(tag)
        else:
            if S.is_empty():
                return False
            if tag[1:] != S.pop():
                return False
        j = raw.find('<', k+1)
    return S.is_empty()

html_string = """ <body>
<center>
<h1> The Little Boat </h1>
</center>
<p> The storm tossed the little
boat like a cheap sneaker in an
old washing machine. The three
drunken fishermen were used to
such treatment, of course, but
not the tree salesman, who even as
a stowaway now felt that he
had overpaid for the voyage. </p>
<ol>
<li> Will the salesman die? </li>
<li> What color is the boat? </li>
<li> And what about Naomi? </li>
</ol>
</body>"""

print(is_matched_html(html_string))
html_string2 = """ <body>
<center>
<h1> The Little Boat </h1>
</center>
 <a href="https://www.w3schools.com">This is a link</a> 
<p> The storm tossed the little
boat like a cheap sneaker in an
old washing machine. The three
drunken fishermen were used to
such treatment, of course, but
not the tree salesman, who even as
a stowaway now felt that he
had overpaid for the voyage. </p>
<ol>
<li> Will the salesman die? </li>
<li> What color is the boat? </li>
<li> And what about Naomi? </li>
</ol>
</body>"""
print(is_matched_html(html_string2))
#-----------------------------------------------6.20-------------------------------------------------------------
#  6.20

def find_permutations_stack(n):
    nums = {x for x in range(1, n+1, 1)}
    S = ArrayStack()  #Need Stack from R6-3

    for num in nums:
        S.push(([num], nums-set([num])))
    
    while not S.is_empty():
        l, remaining = S.pop()
        if len(remaining) == 0:
            print (l)
        else:
            for n in remaining:
                l2 = l.copy()
                l2.append(n)
                S.push((l2, nums-set(l2)))

def find_permutations_stack2(n):
    nums = {x for x in range(1, n+1, 1)}
    S = ArrayStack()  

    for num in nums:
        S.push(([num], nums-set([num])))
    i = 0
    j = 0
    while not S.is_empty():
        i += 1
        #print("S---pre-pop", str(S))
        l, remaining = S.pop()
        #print("l---, remaining", l, remaining)
        #print("S---post-pop", str(S))
        if len(remaining) == 0:
            print ('result', l)
        else:
            for n in remaining:
                j += 1
                l2 = l.copy()
                l2.append(n)
                #print("---l2---", l2)
                S.push((l2, nums-set(l2)))
                #print("---S---", str(S))
        
    print('i', i, 'j', j)
    
find_permutations_stack(5)
find_permutations_stack2(3)
find_permutations_stack2(2)
find_permutations_stack2(4)
find_permutations_stack2(5)
find_permutations_stack2(8)
#-----------------------------------------------6.21-------------------------------------------------------------
#  6.21
"""
see notes
"""

UNK = chr(1000)



def sub_rec(U, S):
    """
    U is the current set
    S is the remaining sequence
    """
    if len(S) == 0:
        print('{', str([x for x in U if x!= UNK])[1:-1], '}')
        
    else:
        val = S.pop()
        U.append(UNK)
        sub_rec(U, S)
        U.pop()
        
        U.append(val)
        sub_rec(U, S)
        U.pop()
        S.append(val)

def print_subsets (U):
    sub_rec([], list(U))
    
    
print_subsets({1,2,3,4,5})


UNK = chr(1000)

def subsets_without_recursion(numbers):
    S = ArrayStack()   #Need Stack from R6-3
    Q = ArrayQueue()   #Need Queue from R6-11
    for element in numbers:
        if Q.is_empty():
            Q.enqueue(set([element]))
            Q.enqueue(set([UNK]))
            
        else:
            #Process all the elements of the Queue
            while not Q.is_empty():
                val = Q.dequeue()
                new_set_1 = val.copy()
                new_set_1.add(element)
                S.push(new_set_1)
                
                new_set_2 = val.copy()
                new_set_2.add(UNK)
                S.push(new_set_2)
                
            #Repopulate the Queue for the next element
            while not S.is_empty():
                Q.enqueue(S.pop())
    
    #Once you are dont the loop, the Queue should be filled with sets
    while not Q.is_empty():
        output = Q.dequeue()
        print ('{', str([x for x in output if x != UNK])[1:-1], '}')
        
        
subsets_without_recursion({1,2,3,4,5})
#-----------------------------------------------6.22-------------------------------------------------------------
#  6.22
def is_matched(expr):
  """Return True if all delimiters are properly match; False otherwise."""
  lefty = '({['                               # opening delimiters
  righty = ')}]'                              # respective closing delims
  S = ArrayStack()
  for c in expr:
    if c in lefty:
      S.push(c)                               # push left delimiter on stack
    elif c in righty:
      if S.is_empty():
        return False                          # nothing to match with
      if righty.index(c) != lefty.index(S.pop()):
        return False                          # mismatched
  return S.is_empty()                         # were all symbols matched?

def arithmetic_expr(raw):
    S = ArrayStack()
    j = raw.find('(')
    while j != -1:
        k = raw.find(')', j+1)
        sp = raw.find(' ', j+1)
        if k == -1:
            return False
        if (sp > 0  and sp < k):
            tag = raw[j+1:sp]
            
        else:
            tag = raw[j+1:k]
        print(tag)
        if not tag.startswith('/'):
            S.push(tag)
        else:
            if S.is_empty():
                return False
            if tag[1:] != S.pop():
                return False
        j = raw.find('<', k+1)
    return S.is_empty()

def test(expr):
    operands = 'ABCDEFGHIJKLMNOPQUSTUVWXYZ'
    operator = '+-/*'
    op_stack = ArrayStack()     # create empty stack for keeping operators
    output = []                 # create an empty list for output
    # convert input infix string to list by using string method split
    input_infix = list(expr)   # ??? is this correct
    output_list = ''
    for token in len(input_infix):
        
        if token in operands:
            output.append()
        if token == '(':
            op_stack.push(token)
        if token == ')':
            tmp = op_stack.pop()
            while not (tmp != '('):
                output.append(tmp)
                tmp = op_stack.pop()
            
    return output
    
post_fix_str = '((5 +2)∗(8 −3))/4'
post_fix_str1 = '(5+2)'

#-----------------------------------------------6.23-------------------------------------------------------------
#  6.23
def ex6_23(R, S, T):
    counter = len(S) + len(T)
    for i in range(len(S)):
        R.push(S.pop())
    for i in range(len(T)):
        R.push(T.pop())
    for i in range(counter):
        S.push(R.pop())
    return 

R = ArrayStack()
S = ArrayStack()
T = ArrayStack()
for i in range(1,4,1):
    R.push(i)
for i in range(4,6,1):
    S.push(i)
for i in range(6,10,1):
    T.push(i)
print('R', R)
print('S',S)
print('T',T)
ex6_23(R,S,T)  
print('-----') 
print('R', R)
print('S',S)
print('T',T)

     
#-----------------------------------------------6.24-------------------------------------------------------------
#  6.24
class ArrayQStack():
    def __init__(self):
        self._data = ArrayQueue()
        self._n = 0 # number of elements
        
    def __len__(self):
        return self._n
    
    def is_empty(self):
        return self._data.is_empty()
    
    def pop(self):
        if self.is_empty():
            raise Empty('Cannot pop from empty stack')
        ans = self._data.dequeue()
        self._n -= 1
        return ans
        
    def push(self, value):
        self._data.enqueue(value)
        self._n += 1
        for i in range(self._n - 1):
            self._data.enqueue(self._data.dequeue())
        
    def top(self):
        return self._data.first()
        
    def __str__(self):
        return str(self._data)
        
    
if __name__ == '__main__':
    aqstk = ArrayQStack()
    aqstk.push('A')
    aqstk.push('B')
    aqstk.push('C')
    print(aqstk.pop())
    print(aqstk.pop())
    print(aqstk.pop())
#-----------------------------------------------6.25-------------------------------------------------------------
#  6.25
class Empty(Exception):
    pass

class ArraySQueue():
    def __init__(self):
        self._dstack = ArrayStack()
        self._nd = 0
        self._estack = ArrayStack()
        self._ne = 0
        
    def __len__(self):
        return self._nd + self._ne
    
    def is_empty(self):
        return (self._nd + self._ne == 0)
    
    def enqueue(self, value):
        self._estack.push(value)
        self._ne += 1
        
    def _stack_transfer(self):
        while self._ne > 0:
            self._dstack.push(self._estack.pop())
            self._ne -= 1
            self._nd += 1
            
    def dequeue(self):
        # If the dstack (dequeue stack) is empty, pop all 
        # values over from the estack (enqueue stack)
        if self._nd == 0:
            if self._ne == 0: raise Empty('Your queue is empty!')
            self._stack_transfer()
        
        ans = self._dstack.pop()
        self._nd -= 1
        return ans
    
    def first(self):
        if self._nd == 0:
            if self._ne == 0: raise Empty('Your queue is empty!')
            self._stack_transfer()
        return self._dstack.top()
    
if __name__ == '__main__':
    que = ArraySQueue()
    que.enqueue('A')
    que.enqueue('B')
    que.enqueue('C')
    print(que.dequeue())
    print(que.dequeue())
    print(que.dequeue())
    que.enqueue('A')
    que.enqueue('B')
    print(que.dequeue())
    que.enqueue('C')
    que.enqueue('D')
    print(que.dequeue())
    print(que.dequeue())
    print(que.dequeue())
    
#-----------------------------------------------6.26-------------------------------------------------------------
#  6.26
# Implement double ended queue using two stacks
class DoubleEndedQueueW2Stacks():

    def __init__(self):
        self._last_stk_data = ArrayStack()
        self._n_last = 0
        self._first_stk_data = ArrayStack()
        self._n_first = 0
        
    def add_first(self, e):
        if (self._n_last > 0):
            self._stack_transfer_to_first_stk()
        self._first_stk_data.push(e)
        self._n_first += 1
        
    def delete_first(self):
        if (self._n_first == 0 and self._n_last == 0):
            raise Empty('Empty Queue - nothing to delete')
        if (self._n_last > 0):
            self._stack_transfer_to_first_stk()
        ans = self._first_stk_data.pop()
        self._n_first -= 1
        return ans

    def first(self):
        if (self._n_first == 0 and self._n_last == 0):
            raise Empty('Empty Queue - nothing to return')
        if (self._n_last > 0):
            self._stack_transfer_to_first_stk()
        return self._first_stk_data.top()

    def add_last(self, e):
        if (self._n_first > 0) :
            self._stack_transfer_to_last_stk()
        self._last_stk_data.push(e)
        self._n_last += 1
        
    def delete_last(self):
        if (self._n_first == 0 and self._n_last == 0):
            raise Empty('Empty Queue - nothing to delete')
        if (self._n_first > 0) :
            self._stack_transfer_to_last_stk()
        ans = self._last_stk_data.pop()
        self._n_last -= 1
        return ans
        
    def last(self):
        if (self._n_first == 0 and self._n_last == 0):
            raise Empty('Empty Queue - nothing to return')
        if (self._n_first > 0):
            self._stack_transfer_to_last_stk()
        return self._last_stk_data.top()

    def is_empty(self):
        return (self._n_first + self._n_last == 0)        
    
    def __len__(self):
        return (self._n_first + self._n_last)        

    def _stack_transfer_to_last_stk(self):
        # some checks here ?????
        for i in range(self._n_first):
            self._last_stk_data.push(self._first_stk_data.pop())
            self._n_last += 1
            self._n_first -= 1

    def _stack_transfer_to_first_stk(self):
        # some checks here ?????
        for i in range(self._n_last):
            self._first_stk_data.push(self._last_stk_data.pop())
            self._n_first += 1
            self._n_last -= 1

if __name__ == '__main__':
    dblQ = DoubleEndedQueueW2Stacks()
    dblQ.add_first('C')
    dblQ.add_first('B')
    dblQ.add_first('A')
    print(dblQ.delete_first())
    print(dblQ.delete_last())
    dblQ.add_last('D')
    dblQ.add_last('E')
    print(dblQ.delete_first())
    print(dblQ.delete_last())
    
  
#-----------------------------------------------6.27-------------------------------------------------------------
#  6.27
class ArrayStackContains():
    
    def __init__(self):
        self._data = ArrayStack()
        self._dataQ = ArrayQueue()
        self._n = 0
        
    def is_empty(self):
        return (self._n == 0)
    
    def __len__(self):
        return (self._n)
    
    def pop(self):
        if self.is_empty():
            raise Empty('Stack is empty.  Nothing to return')
        ans = self._data.pop()
        self._n -= 1
        return ans
        
    def push(self, e):
        self._data.push(e)
        self._n += 1
        
    def contains(self, e):
        result = False
        for i in range(self._n):
            val = self._data.pop()
            if (val == e):
                result = True
            self._dataQ.enqueue(val)
        for i in range(self._n): # this will be in reverse order
            self._data.push(self._dataQ.dequeue())
        for i in range(self._n):
            self._dataQ.enqueue(self._data.pop())
        for i in range(self._n): # this will correct the order
            self._data.push(self._dataQ.dequeue())
        
        return result
    
    def __str__(self):
        return str(self._data)

if __name__ == '__main__':
    x = ArrayStackContains()
    x.push('A')
    x.push('B')
    x.push('C')
    x.push('D')
    print(str(x))
    print('popped', x.pop())
    print(str(x))
    print(x.contains('B'))
    print(str(x))
    print(x.contains('D'))
    print(str(x))
    print('popped', str(x.pop()))
    print(str(x))
    print('popped', x.pop())
    print(str(x))
    print('popped', x.pop())
    print(str(x))
    print('popped', x.pop())
    print(str(x))
    
    
#-----------------------------------------------6.28-------------------------------------------------------------
#  6.28

class Empty(Exception):
    """ Error raised when attempting to access an element from an empty container"""
    pass

class Full(Exception):
    """ Error raised when attempting to access an element from an empty container"""
    pass

class ArrayQueueMax:
    DEFAULT_CAPACITY = 10
    
    def __init__(self, cap_limit = None):
        self._data = [None]* ArrayQueue.DEFAULT_CAPACITY
        if cap_limit is None:
            self._cap_limit = 40
        self._size = 0
        self._front = 0
    
    def __len__(self):
        """ Return number of elements in the queue"""
        return self._size
    
    def is_empty(self):
        return self._size == 0
    
    def first(self):
        """ Return w/o removing first element of Q front"""
        if self.is_empty():
            raise Empty("Queue is empty")
        return self._data[self._front]
            
    def dequeue(self):
        """ Return and remove first element of Q front"""
        if self.is_empty():
            raise Empty("Queue is empty")
        answer = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        #if 0 < self._size < len(self._data) // 4:
        #    self._resize(  len(self._data) // 2)
        return answer
    
    def enqueue(self, e):
        """ Add an element to the back of the queue"""
        if self._size == len(self._data):
            if (2 * len(self._data) > self._cap_limit):
                raise Full('Queue is full - it has reached capacity of', self._cap_limit)            
            self._resize(2 * len(self._data))
        queuing_pt = (self._front + self._size) % len(self._data)
        self._data[queuing_pt] = e
        self._size += 1
    
    def _resize(self, cap):
        """ resize to new list with new capacity """
        print('Resizing to new capacity', cap)
        olddata = self._data
        self._data = [None] * cap
        copy_position = self._front
        for i in range(self._size):
            self._data[i] = olddata[copy_position]
            copy_position = (copy_position + 1) % len(olddata)
        self._front = 0
        #print((self._front + self._size) % len(self._data))
        
    def __str__(self):
        """Produce string representation of vector."""
        return str(self._data)  # adapt list representation
    
if __name__ == '__main__':
    B = ArrayQueueMax()
    for i in range(41):
        B.enqueue(chr(65+i))
        print(str(B))
#-----------------------------------------------6.29-------------------------------------------------------------
#  6.29

class Empty(Exception):
    """ Error raised when attempting to access an element from an empty container"""
    pass
class Full(Exception): pass

class ArrayRotateQueue:
    DEFAULT_CAPACITY = 10
    
    def __init__(self):
        self._data = [None]* ArrayQueue.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0
    
    def __len__(self):
        """ Return number of elements in the queue"""
        return self._size
    
    def is_empty(self):
        return self._size == 0
    
    def first(self):
        """ Return w/o removing first element of Q front"""
        if self.is_empty():
            raise Empty("Queue is empty")
        return self._data[self._front]
            
    def dequeue(self):
        if self.is_empty():
            raise Empty("Queue is empty")
        answer = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        return answer
    
    def enqueue(self, e):
        """ Add an element to the back of the queue"""
        if self._size == len(self._data): 
            self._resize(self._size * 2)
        self._data[(self._front + self._size)%len(self._data)] = e
        self._size += 1
    
    def rotate(self):
        if self.is_empty(): raise Empty('The array is empty')
        self._data[(self._front + self._size)%len(self._data)] = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1)%len(self._data)
        
    def _resize(self, cap):
        """ resize to new list with new capacity """
        new_array = [None]*cap
        for i in range(self._size):
            new_array[i] = self._data[(self._front + i)%len(self._data)]
        self._data = new_array
        self._front = 0
        
    def __str__(self):
        """Produce string representation of vector."""
        return str(self._data)  # adapt list representation
        
if __name__ == '__main__':
    arq = ArrayRotateQueue()
    arq.enqueue('A')
    arq.enqueue('B')
    arq.enqueue('C')
    arq.enqueue('D')
    arq.enqueue('E')
    print(str(arq))
    arq.dequeue()
    print(str(arq))
    arq.enqueue('F')
    print(str(arq))
    print('------------')
    arq.rotate()
    print(str(arq))
    arq.rotate()
    print(str(arq))
    arq.rotate()
    print(str(arq))
    arq.rotate()
    print(str(arq))
    arq.rotate()
    print(str(arq))
    arq.rotate()
    print(str(arq))
    arq.rotate()
    print(str(arq))

#-----------------------------------------------6.30-------------------------------------------------------------
#  6.30
import random

def play_queue_game(Q, R, num_turns = 100, max_rotations = 20):
    for _ in range(num_turns):
        current_array = Q if random.random()>0.5 else R
        for _ in range(random.randint(0, max_rotations)):
            final_processed_value = current_array.first() 
            current_array.rotate()
            
    return final_processed_value % 2 == 0




Q, R = ArrayRotateQueue(), ArrayRotateQueue()

Q.enqueue(0)

for i in range(1, 100):
    R.enqueue(i)
    

total_wins = 0
num_games = 1000
for game in range(num_games):
    if play_queue_game(Q, R): total_wins+=1
        
        
print(f'Alice won {total_wins/num_games*100}% of her games')
#-----------------------------------------------6.31-------------------------------------------------------------
#  6.31
""" 
Mazie = 2 m
Daisy = 4 m
Crazy = 10 m
Lazy = 20 m
Total time = 34 m
Mazie + Daisy forward          round time:  4 m     total time:  4 m
Mazie back                     round time:  2 m     total time:  6 m
Crazy + Lazy forward           round time: 20 m     total time: 26 m
Daisy back                     round time:  4 m     total time: 30 m
Mazie + Daisy forward          round time:  4 m     total time: 34 m
"""
#-----------------------------------------------6.32-------------------------------------------------------------
#  6.32
"""
ArrayDeque implementation 
"""
class Empty(Exception):
    """ Error raised when attempting to access an element from an empty container"""
    pass

class ArrayDequeCustom():
    DEFAULT_CAPACITY = 10
    
    def __init__(self):
        self._data = [None]* ArrayQueue.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0
        #self._back = 0
    
    def __len__(self):
        """ Return number of elements in the queue"""
        return self._size
    
    def is_empty(self):
        return self._size == 0
    
    def first(self):
        """ Return w/o removing first element of Q front"""
        if self.is_empty():
            raise Empty("Queue is empty")
        print(self._front, self._data[self._front])
        return self._data[self._front]

    def last(self):
        """ Return w/o removing last element of Q end"""
        if self.is_empty():
            raise Empty("Queue is empty")
        back = (self._front + self._size - 1) % len(self._data)
        return self._data[back]
                        
    def delete_first(self):
        """ Return and remove first element of Q front"""
        if self.is_empty():
            raise Empty("Queue is empty")
        answer = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        #self._back = (self._front + self._size - 1) % len(self._data)
        return answer
    
    def delete_last(self):
        """ Return and remove the last element of the Q back"""
        if self.is_empty():
            raise Empty('Queue is empty.  Nothing to delete')
        back = (self._front + self._size - 1) % len(self._data)
        answer = self._data[back]
        self._data[back] = None
        self._size -= 1
        return answer
        
    def add_first(self, e):
        """ add element to the front of the queue"""
        if self._size == len(self._data):
            self._resize(2 * len(self._data))
        self._front = (self._front - 1) % len(self._data)
        self._data[self._front] = e
        self._size += 1
    
    def add_last(self, e):
        """ add_last same as queue enqueue"""
        if self._size == len(self._data):
            self._resize(2 * len(self._data))
        queuing_pt = (self._front + self._size) % len(self._data)
        self._data[queuing_pt] = e
        self._size += 1
    
    def _resize(self, cap):
        """ resize to new list with new capacity """
        print('Resizing to new capacity', cap)
        olddata = self._data
        self._data = [None] * cap
        copy_position = self._front
        for i in range(self._size):
            self._data[i] = olddata[copy_position]
            copy_position = (copy_position + 1) % len(olddata)
        self._front = 0
        
    def __str__(self):
        """Produce string representation of vector."""
        return str(self._data)  # adapt list representation
         
if __name__ == '__main__':
    adc = ArrayDequeCustom()
    adc.add_last(5)
    print(str(adc))
    adc.add_first(3)
    print(str(adc))
    adc.add_first(7)
    print(str(adc))
    print(adc.first())
    print(adc.last())
    adc.delete_last()
    print(str(adc))
    print(len(adc))
    adc.delete_last()
    print(str(adc))
    adc.delete_last()
    print(str(adc))
    adc.add_first(6)
    print(str(adc))
    adc.last()
    adc.add_first(8)
    print(str(adc))
    print(adc.is_empty())
    print(adc.last())
    print(str(adc))
#-----------------------------------------------6.33-------------------------------------------------------------
#  6.33
"""
We have to support the following methods:
len
appendleft
append
popleft
pop
D[0]            --> via __getitem__(self, index)
D[-1]
D[j]
D[j] = val      --> via __setitem__(self, index, value)
D.clear()
D.rotate(k)
D.remove(e)
D.count(e)
"""
class Empty(Exception):
    """ Error raised when attempting to access an element from an empty container"""
    pass

class ArrayDequeMaxLen():
    DEFAULT_CAPACITY = 10
    
    def __init__(self, maxlen = None):
        self._data = [None]* ArrayQueue.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0
        self._maxlen = maxlen
    
    def __len__(self):
        """ Return number of elements in the queue"""
        return self._size
    
    def is_empty(self):
        return self._size == 0
    
    def __getitem__(self, index):  # same as D[0]
        """ Get item at particular index"""
        # handle negative indices
        if index < 0: 
            index = self._size + index
        if not (0 <= index < self._size):
            raise IndexError('Invalid index')
        return self._data[(self._front + index) % len(self._data)]

    def __setitem__(self, index, value):   
        """ set value of item """
        if index < 0: 
            index = self._size + index
        if not (0 <= index < self._size):
            raise IndexError('Invalid index')
        self._data[(self._front + index) % len(self._data)] = value
                        
    def popleft(self):
        """ Return and remove first element of Q front"""
        if self.is_empty():
            raise Empty("Queue is empty")
        answer = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        #self._back = (self._front + self._size - 1) % len(self._data)
        return answer
    
    def pop(self):
        """ Return and remove the last element of the Q back"""
        if self.is_empty():
            raise Empty('Queue is empty.  Nothing to delete')
        back = (self._front + self._size - 1) % len(self._data)
        answer = self._data[back]
        self._data[back] = None
        self._size -= 1
        return answer
        
    def appendleft(self, e):
        """ add element to the front of the queue"""
        if self._size == len(self._data):
            self._resize(2 * len(self._data))
        self._front = (self._front - 1) % len(self._data)
        self._data[self._front] = e
        self._size += 1
    
    def append(self, e):
        """ add_last same as queue enqueue"""
        if self._size == len(self._data):
            self._resize(2 * len(self._data))
        queuing_pt = (self._front + self._size) % len(self._data)
        self._data[queuing_pt] = e
        self._size += 1
    
    def _resize(self, cap):
        """ resize to new list with new capacity """
        # print('Resizing to new capacity', cap)
        if (self._maxlen is not None):
            cap = min(cap, self._maxlen)
        olddata = self._data
        self._data = [None] * cap
        copy_position = self._front
        for i in range(self._size):
            self._data[i] = olddata[copy_position]
            copy_position = (copy_position + 1) % len(olddata)
        self._front = 0
        
    def __str__(self):
        """Produce string representation of vector."""
        return str(self._data)  # adapt list representation
    
    def clear(self):
        self._data = [None] * len(self._data)
        self._size = 0
        self._front = 0
        
    def count(self, e):
        count = 0
        for i in range(self._size):
            if (self._data[(self._front + i) % len(self._data)] == e):
                count += 1
        return count

    # def count(self, value):
    #     if self.is_empty(): raise Empty('Deque is empty')
    #     total_count = 0
    #     for i in range(self._size):
    #         ans = self.pop()
    #         if ans == value: total_count+= 1
    #         self.appendleft(ans)
            
    #     return total_count
        
    def remove(self, value):
        if self.is_empty(): raise Empty('Deque is empty')
        found  = False
        for i in range(self._size):
            ans = self.pop()
            if ans == value and not found:
                found = True  #Do not remove subsequent finds
            else: self.appendleft(ans)
                
    def rotate(self, k):
        for _ in range(k):
            ans = self.pop()
            self.appendleft(ans)
       
if __name__ == '__main__':
    AQM = ArrayDequeMaxLen(20)
    
    print('Adding last')
    for i in range(100):
        AQM.append(i)
        print (i, AQM._data)
        
    print('\nDelete 80', AQM.remove(80), AQM._data, AQM._front)
        
    AQM.clear()
    print('\nCleared Data:', AQM._data)
    
    for i in range(100):
        AQM.append(i%3)
      
    print('\nFound', AQM.count(2), '2s in ', AQM._data)    
    
        
    print ('\nAdding first')
    for i in range(20, 10, -1):
        AQM.appendleft(i)
        print (i, AQM._data)
        
    print(AQM._front)
        
    print ('\nRotating')    
    for i in range(20):
        AQM.rotate(1)
        print('Front is:', AQM[0])
        
    print('\nPerforming the removals')
    while not AQM.is_empty():
        print ('Remove first', AQM[0], AQM.popleft(), 'Remove last', AQM[-1],  AQM.pop())
        
#-----------------------------------------------6.34-------------------------------------------------------------
#  6.34
""" evaluate postfix notation eg: "(A+B)*(C+D) is A B + C D + *"
"""
import ArrayStack

def postFix_eval(postfix_expr):
    operand_stack = ArrayStack()
    token_list = postfix_expr.split()
    for token in token_list:
        if (token not in '+-*/') and (not token.isnumeric()) :
            raise Exception('Invalid token')
    print(token_list)
    for token in token_list:
        print('token', str(operand_stack))
        if token in "0123456789": 
            operand_stack.push(int(token))
        else:
            operand2 = operand_stack.pop()
            operand1 = operand_stack.pop()
            result = do_math(token, operand1, operand2)
            operand_stack.push(result)
    return operand_stack.pop()

def postFix_eval_any_int(postfix_expr):
    operand_stack = ArrayStack()
    token_list = postfix_expr.split()
    for token in token_list:
        if (token not in '+-*/') and (not token.isnumeric()) :
            raise Exception('Invalid token')
    print(token_list)
    for token in token_list:
        print('token', str(operand_stack))
        if token not in "+-*/": 
            operand_stack.push(int(token))
        else:
            operand2 = operand_stack.pop()
            operand1 = operand_stack.pop()
            result = do_math(token, operand1, operand2)
            operand_stack.push(result)
    return operand_stack.pop()

def do_math(op, op1, op2):
    if (op == '*'):
        return op1 * op2
    if (op == '/'):
        return op1 / op2
    if (op == '-'):
        return op1 - op2
    if (op == '+'):
        return op1 + op2    

print(postFix_eval('7 8 + 3 2 + /'))
print(postFix_eval_any_int('100 8 + 3 2 + /')) # fails because it fails condition 
# token in "0123456789": resutling in an empty stack thus ending throwing an error

#-----------------------------------------------6.35-------------------------------------------------------------
#  6.35
""" Leaky stack using 6.16 --> No Full exception raised 
    also Ctrl+Z does not throw Empty exception - so will not throw that either
"""
class Empty(Exception):
    """ Error raised when attempting to access an element from an empty container"""
    pass

class LeakyArrayStack:
    """ LIFO Stack implementation using a Python list as underlying storage"""
    def __init__(self, cap=None):
        """ Create an empty stack """
        self._data = []
        if cap is None: cap = 15
        self._max_capacity = cap
        
    def __len__(self):
        """ Returns number of elements in stack """
        return len(self._data)
    
    def is_empty(self):
        """ Return True if the stack is empty """
        return len(self._data) == 0
        
    def push(self, e):
        """ Add element e to the top of the stack """
        if len(self._data) >= self._max_capacity:
            # Leaky stack push first one out and keep the last one
            for i in range(len(self._data) - 1):
                self._data[i] = self._data[i + 1] 
            self._data.pop()
        self._data.append(e)
        
    def top(self):
        """ Return (but do not remove) element at top of stack. If empty - raise Exception"""
        if self.is_empty():
            return  # Not throwing Empty exception for Empty stack
        return self._data[-1]       # return last item in the list
        
    def pop(self):
        """ Remove and return element at top of stack. If empty - raise Exception"""
        if self.is_empty():
            return  # Not throwing Empty exception for Empty stack
        return self._data.pop()       # return last item in the list
    
    def __str__(self):
        """Produce string representation of vector."""
        return str(self._data)  # adapt list representation

        
if __name__ == '__main__':
    stk = LeakyArrayStack(15)
    for i in range(20):
        stk.push(i)
        print(stk)

#-----------------------------------------------6.36-------------------------------------------------------------
#  6.36
# pass in list of tuples containing # shares and share price
# eg. [(100, 69.38), (200, 75.25), (50, 68.51), (300, 80.16)] - shares that were purchased
# another sell list eg. [(150, 85.63)] to compute capital gains


def compute_cap_gain(buyQ, sellQ):
    sellShares, sellPrice = sellQ.dequeue()
    capGain = 0
    remainingToSell = sellShares
    remainingtoQ = 0
    
    while (remainingToSell > 0 ): #problem if list already popped
        print('remainingToSell', remainingToSell)
        buyShares, buyPrice = buyQ.dequeue()
        if buyShares <= remainingToSell:
            remainingToSell -= buyShares
            capGain += buyShares * (sellPrice - buyPrice)
            
        else:
            remainingtoQ = (buyShares - remainingToSell)
            capGain += (remainingToSell) * (sellPrice - buyPrice)
            buyQ.enqueue((remainingtoQ, buyPrice))
            for i in range(len(buyQ)-1):
                buyQ.rotate()
            break
    return capGain

buylist = [(100, 69.38), (200, 75.25), (50, 68.51), (300, 80.16)]
selllist = [(150, 85.63)]
posQ = ArrayRotateQueue()
sellQ = ArrayRotateQueue()

for txn in buylist:
    posQ.enqueue(txn)
print(posQ)
sellQ.enqueue(selllist[0])
print(sellQ)
print(compute_cap_gain(posQ, sellQ))

#-----------------------------------------------6.37-------------------------------------------------------------
#  6.37
# manage red and blue stacks in same array
# challenges - collisions
#            - resize

class Empty(Exception): pass

class ArrayDoubleStack():
    INITIAL_CAPACITY = 20

    def __init__(self):
        self._data = [None]*self.INITIAL_CAPACITY
        self._size_r = 0
        self._size_b = 0
        self._front_r = 0
        self._front_b = ArrayDoubleStack.INITIAL_CAPACITY // 2

    def is_empty_red(self):
        return self._size_r == 0

    def is_empty_blue(self):
        return self._size_b == 0
    
    def is_full(self):
        return (self._size_r + self._size_b) == len(self._data)

    def push_red(self, value):
        loc = (self._front_r + self._size_r) % len(self._data)
        if (self.is_full() or loc == self._front_b) : 
            self._resize(len(self._data) * 2)
        new_loc = (self._front_r + self._size_r) % len(self._data)
        self._data[new_loc] = value
        self._size_r += 1
        
    def push_blue(self, value):
        loc = (self._front_b + self._size_b) % len(self._data)
        if (self.is_full() or loc == self._front_r) : 
            self._resize(len(self._data) * 2)
        new_loc = (self._front_b + self._size_b) % len(self._data)
        self._data[new_loc] = value
        self._size_b += 1
        
    def pop_red(self):
        if self.is_empty_red(): raise Empty('Red is empty')
        ans = self._pop(self._front_r, self._size_r)
        self._size_r -= 1
        return ans
        
    def pop_blue(self):
        if self.is_empty_blue(): raise Empty('Blue is empty')
        ans = self._pop(self._front_b, self._size_b)
        self._size_b -= 1
        return ans        

    def _pop(self, front, size):
        ans = self._data[(front + size - 1) % len(self._data)]
        self._data[(front + size - 1) % len(self._data)] = None
        return ans

    def _resize(self, capacity):
        newArray = [None]* capacity
        for i in range(self._size_r):
            newArray[i] = self._data[self._front_r + i % len(self._data)]
            
        new_front_b = self._size_r + (capacity - self._size_r-self._size_b) // 2
            
        for i in range(self._size_b):
            newArray[i + new_front_b] = self._data[self._front_b + i % len(self._data)]

        self._front_r = 0
        self._front_b = new_front_b
        self._data = newArray
        
    def __str__(self):
        return str(self._data)
        
if __name__ -- '__main__':
    dA = ArrayDoubleStack()
        
    for i in range(11):
        dA.push_blue(i)
        dA.push_red(100+i)
        print(dA._data, dA._size_r, dA._size_b, '\n')
    print(dA)   
    while not dA.is_empty_red():
        print (dA.pop_red())
    
    print(dA)
    