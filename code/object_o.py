# -*- coding: utf-8 -*-
"""



"""
# R-2.4
# ---------------------------------------------------------------------------
class Flower:
  """A consumer credit card."""
  
  def __init__(self, name, petals, price):
    """Create a new flower instance.
    
    """
    self._name = name
    self._petals = petals
    self._price = price

  def set_name(self, value):
      self._name = value
        
  def get_name(self):
      return self._name        
  
  def set_petals(self, value):
      self._petals = value
        
  def get_petals(self):
      return self._petals        

  def set_price(self, value):
      self._price = value
        
  def get_price(self):
      return self._price

  name = property(get_name,set_name)    
  petals = property(get_petals,set_petals)   
  price = property(get_price,set_price)           
  
f= Flower("Rose", 26, 10)  
(f.name, f.petals, f.price)
#Out[47]: ('Rose', 26, 10)
f.name= "Lily"
f.petals=28
f.price=12
(f.name, f.petals, f.price)
#Out[51]: ('Lily', 28, 12)

# R-2.5
# ---------------------------------------------------------------------------
class CreditCard:
  """A consumer credit card."""
  
  def __init__(self, customer, bank, acnt, limit):
    """Create a new credit card instance.

    The initial balance is zero.

    customer  the name of the customer (e.g., 'John Bowman')
    bank      the name of the bank (e.g., 'California Savings')
    acnt      the acount identifier (e.g., '5391 0375 9387 5309')
    limit     credit limit (measured in dollars)
    """
    self._customer = customer
    self._bank = bank
    self._account = acnt
    self._limit = limit
    self._balance = 0

  def get_customer(self):
    """Return name of the customer."""
    return self._customer
    
  def get_bank(self):
    """Return the bank's name."""
    return self._bank

  def get_account(self):
    """Return the card identifying number (typically stored as a string)."""
    return self._account

  def get_limit(self):
    """Return current credit limit."""
    return self._limit

  def get_balance(self):
    """Return current balance."""
    return self._balance

  def charge(self, price):
    """Charge given price to the card, assuming sufficient credit limit.

    Return True if charge was processed; False if charge was denied.
    """
    if not isinstance(price, (int, float) ):
        raise ValueError("price must be a valid number")
    
    if price + self._balance > self._limit:  # if charge would exceed limit,
      return False                           # cannot accept charge
    else:
      self._balance += price
      return True

  def make_payment(self, amount):
    """Process customer payment that reduces balance."""
    if not isinstance(amount, (int, float) ):
        raise ValueError("price must be a valid number")
    
    self._balance -= amount

# R-2.6
# ---------------------------------------------------------------------------
class CreditCard:
  """A consumer credit card."""
  
  def __init__(self, customer, bank, acnt, limit):
    """Create a new credit card instance.

    The initial balance is zero.

    customer  the name of the customer (e.g., 'John Bowman')
    bank      the name of the bank (e.g., 'California Savings')
    acnt      the acount identifier (e.g., '5391 0375 9387 5309')
    limit     credit limit (measured in dollars)
    """
    self._customer = customer
    self._bank = bank
    self._account = acnt
    self._limit = limit
    self._balance = 0

  def get_customer(self):
    """Return name of the customer."""
    return self._customer
    
  def get_bank(self):
    """Return the bank's name."""
    return self._bank

  def get_account(self):
    """Return the card identifying number (typically stored as a string)."""
    return self._account

  def get_limit(self):
    """Return current credit limit."""
    return self._limit

  def get_balance(self):
    """Return current balance."""
    return self._balance

  def charge(self, price):
    """Charge given price to the card, assuming sufficient credit limit.

    Return True if charge was processed; False if charge was denied.
    """
    if not isinstance(price, (int, float) ):
        raise ValueError("price must be a valid number")
    
    if price + self._balance > self._limit:  # if charge would exceed limit,
      return False                           # cannot accept charge
    else:
      self._balance += price
      return True

  def make_payment(self, amount):
    """Process customer payment that reduces balance."""
    if not isinstance(amount, (int, float) ) or amount < 0:
        raise ValueError("price must be a valid number")
    
    self._balance -= amount

# R-2.7
# ---------------------------------------------------------------------------
class CreditCard:
  """A consumer credit card."""
  
  def __init__(self, customer, bank, acnt, limit, balance = 0):
    """Create a new credit card instance.

    The initial balance is zero.

    customer  the name of the customer (e.g., 'John Bowman')
    bank      the name of the bank (e.g., 'California Savings')
    acnt      the acount identifier (e.g., '5391 0375 9387 5309')
    limit     credit limit (measured in dollars)
    """
    self._customer = customer
    self._bank = bank
    self._account = acnt
    self._limit = limit
    self._balance = balance

  def get_customer(self):
    """Return name of the customer."""
    return self._customer
    
  def get_bank(self):
    """Return the bank's name."""
    return self._bank

  def get_account(self):
    """Return the card identifying number (typically stored as a string)."""
    return self._account

  def get_limit(self):
    """Return current credit limit."""
    return self._limit

  def get_balance(self):
    """Return current balance."""
    return self._balance

  def charge(self, price):
    """Charge given price to the card, assuming sufficient credit limit.

    Return True if charge was processed; False if charge was denied.
    """
    if not isinstance(price, (int, float) ):
        raise ValueError("price must be a valid number")
    
    if price + self._balance > self._limit:  # if charge would exceed limit,
      return False                           # cannot accept charge
    else:
      self._balance += price
      return True

  def make_payment(self, amount):
    """Process customer payment that reduces balance."""
    if not isinstance(amount, (int, float) ) or amount < 0:
        raise ValueError("price must be a valid number")
    
    self._balance -= amount
# R-2.8
# ---------------------------------------------------------------------------
#==Chp2: R-2.8============      
if __name__ == '__main__':
  wallet = []
  wallet.append(CreditCard('John Bowman', 'California Savings',
                           '5391 0375 9387 5309', 2500) )
  wallet.append(CreditCard('John Bowman', 'California Federal',
                           '3485 0399 3395 1954', 3500) )
  wallet.append(CreditCard('John Bowman', 'California Finance',
                           '5391 0375 9387 5309', 5000) )
  for val in range(1, 25):
    print(0,wallet[0].get_balance(),
          wallet[0].get_limit(),  val, 
          wallet[0].charge(val),
          wallet[0].get_balance())
    print(1,wallet[1].get_balance(),
          wallet[1].get_limit(), 20*val, 
          wallet[1].charge(20*val),
          wallet[1].get_balance())
    print(2, wallet[2].get_balance(),
          wallet[2].get_limit(), 30*val, 
          wallet[2].charge(30*val),
          wallet[2].get_balance())    

# R-2.9
# ---------------------------------------------------------------------------

class Vector:
  """Represent a vector in a multidimensional space."""

  def __init__(self, d):
    if isinstance(d, int):
      self._coords = [0] * d
    else:                                  
      try:                                     # we test if param is iterable
        self._coords = [val for val in d]
      except TypeError:
        raise TypeError('invalid parameter type')

  def __len__(self):
    """Return the dimension of the vector."""
    return len(self._coords)

  def __getitem__(self, j):
    """Return jth coordinate of vector."""
    return self._coords[j]

  def __setitem__(self, j, val):
    """Set jth coordinate of vector to given value."""
    self._coords[j] = val



  def __sub__(self, other):
    """Return diff of two vectors."""
    if len(self) != len(other):          # relies on __len__ method
      raise ValueError('dimensions must agree')
    result = Vector(len(self))           # start with vector of zeros
    for j in range(len(self)):
      result[j] = self[j] - other[j]
    return result



# R-2.10
# ---------------------------------------------------------------------------


class Vector:
  """Represent a vector in a multidimensional space."""

  def __init__(self, d):
    if isinstance(d, int):
      self._coords = [0] * d
    else:                                  
      try:                                     # we test if param is iterable
        self._coords = [val for val in d]
      except TypeError:
        raise TypeError('invalid parameter type')

  def __len__(self):
    """Return the dimension of the vector."""
    return len(self._coords)

  def __getitem__(self, j):
    """Return jth coordinate of vector."""
    return self._coords[j]

  def __setitem__(self, j, val):
    """Set jth coordinate of vector to given value."""
    self._coords[j] = val




#==Chp2: R-2.10============     
  def __neg__(self):
    """Return neg of the vector."""
    result = Vector(len(self))           # start with vector of zeros
    for j in range(len(self)):
      result[j] = -self[j]
    return result




# R-2.11
# ---------------------------------------------------------------------------

class Vector:
  """Represent a vector in a multidimensional space."""

  def __init__(self, d):
    if isinstance(d, int):
      self._coords = [0] * d
    else:                                  
      try:                                     # we test if param is iterable
        self._coords = [val for val in d]
      except TypeError:
        raise TypeError('invalid parameter type')

  def __len__(self):
    """Return the dimension of the vector."""
    return len(self._coords)

  def __getitem__(self, j):
    """Return jth coordinate of vector."""
    return self._coords[j]

  def __setitem__(self, j, val):
    """Set jth coordinate of vector to given value."""
    self._coords[j] = val


  def __add__(self, other):
    """Return sum of two vectors."""
    if len(self) != len(other):          # relies on __len__ method
      raise ValueError('dimensions must agree')
    result = Vector(len(self))           # start with vector of zeros
    for j in range(len(self)):
      result[j] = self[j] + other[j]
    return result

  def __radd__(self, other):
    """Return sum of two vectors."""
    if len(self) != len(other):          # relies on __len__ method
      raise ValueError('dimensions must agree')
    result = Vector(len(self))           # start with vector of zeros
    for j in range(len(self)):
      result[j] = self[j] + other[j]
    return result


if __name__ == '__main__':
  # the following demonstrates usage of a few methods
  v = Vector(5)              # construct five-dimensional <0, 0, 0, 0, 0>
  v[1] = 23                  # <0, 23, 0, 0, 0> (based on use of __setitem__)
  v[-1] = 45  
  
  
# R-2.12
# ---------------------------------------------------------------------------

class Vector:
  """Represent a vector in a multidimensional space."""

  def __init__(self, d):
    if isinstance(d, int):
      self._coords = [0] * d
    else:                                  
      try:                                     # we test if param is iterable
        self._coords = [val for val in d]
      except TypeError:
        raise TypeError('invalid parameter type')

  def __len__(self):
    """Return the dimension of the vector."""
    return len(self._coords)

  def __getitem__(self, j):
    """Return jth coordinate of vector."""
    return self._coords[j]

  def __setitem__(self, j, val):
    """Set jth coordinate of vector to given value."""
    self._coords[j] = val


  def __add__(self, other):
    """Return sum of two vectors."""
    if len(self) != len(other):          # relies on __len__ method
      raise ValueError('dimensions must agree')
    result = Vector(len(self))           # start with vector of zeros
    for j in range(len(self)):
      result[j] = self[j] + other[j]
    return result

  def __radd__(self, other):
    """Return sum of two vectors."""
    if len(self) != len(other):          # relies on __len__ method
      raise ValueError('dimensions must agree')
    result = Vector(len(self))           # start with vector of zeros
    for j in range(len(self)):
      result[j] = self[j] + other[j]
    return result
  
  def __mul__(self, multiplier):
      if not isinstance(multiplier, (int, float)):
          raise ValueError('multiplier must be a number')
      
      result = Vector(len(self))
      for j in range(len(self)):
          result[j] = self[j] * multiplier
      return result


if __name__ == '__main__':
  # the following demonstrates usage of a few methods
  v = Vector(5)              # construct five-dimensional <0, 0, 0, 0, 0>
  v[1] = 23                  # <0, 23, 0, 0, 0> (based on use of __setitem__)
  v[-1] = 45  
  
  print(list(v))
  print(list(v * 5))
  print(list(15 * v))  # TypeError: unsupported operand type(s) for *: 'int' and 'Vector'
  
  
# R-2.13
# ---------------------------------------------------------------------------


class Vector:
  """Represent a vector in a multidimensional space."""

  def __init__(self, d):
    if isinstance(d, int):
      self._coords = [0] * d
    else:                                  
      try:                                     # we test if param is iterable
        self._coords = [val for val in d]
      except TypeError:
        raise TypeError('invalid parameter type')

  def __len__(self):
    """Return the dimension of the vector."""
    return len(self._coords)

  def __getitem__(self, j):
    """Return jth coordinate of vector."""
    return self._coords[j]

  def __setitem__(self, j, val):
    """Set jth coordinate of vector to given value."""
    self._coords[j] = val


  def __add__(self, other):
    """Return sum of two vectors."""
    if len(self) != len(other):          # relies on __len__ method
      raise ValueError('dimensions must agree')
    result = Vector(len(self))           # start with vector of zeros
    for j in range(len(self)):
      result[j] = self[j] + other[j]
    return result

  def __radd__(self, other):
    """Return sum of two vectors."""
    if len(self) != len(other):          # relies on __len__ method
      raise ValueError('dimensions must agree')
    result = Vector(len(self))           # start with vector of zeros
    for j in range(len(self)):
      result[j] = self[j] + other[j]
    return result
  
  def __mul__(self, multiplier):
      """ Element wise multiplication """
      if not isinstance(multiplier, (int, float)):
          raise ValueError('multiplier must be a number')
      
      result = Vector(len(self))
      for j in range(len(self)):
          result[j] = self[j] * multiplier
      return result

  def __rmul__(self, multiplier):
      """ Element wise multiplication """
      if not isinstance(multiplier, (int, float)):
          raise ValueError('multiplier must be a number')
      
      result = Vector(len(self))
      for j in range(len(self)):
          result[j] = self[j] * multiplier
      return result
  

if __name__ == '__main__':
  # the following demonstrates usage of a few methods
  v = Vector(5)              # construct five-dimensional <0, 0, 0, 0, 0>
  v[1] = 23                  # <0, 23, 0, 0, 0> (based on use of __setitem__)
  v[-1] = 45  
  
  print(list(v))
  print(list(v * 5))
  print(list(15 * v))  # TypeError: unsupported operand type(s) for *: 'int' and 'Vector'
  

# R-2.14
# ---------------------------------------------------------------------------



class Vector:
  """Represent a vector in a multidimensional space."""

  def __init__(self, d):
    if isinstance(d, int):
      self._coords = [0] * d
    else:                                  
      try:                                     # we test if param is iterable
        self._coords = [val for val in d]
      except TypeError:
        raise TypeError('invalid parameter type')

  def __len__(self):
    """Return the dimension of the vector."""
    return len(self._coords)

  def __getitem__(self, j):
    """Return jth coordinate of vector."""
    return self._coords[j]

  def __setitem__(self, j, val):
    """Set jth coordinate of vector to given value."""
    self._coords[j] = val


  def __add__(self, other):
    """Return sum of two vectors."""
    if len(self) != len(other):          # relies on __len__ method
      raise ValueError('dimensions must agree')
    result = Vector(len(self))           # start with vector of zeros
    for j in range(len(self)):
      result[j] = self[j] + other[j]
    return result

  def __radd__(self, other):
    """Return sum of two vectors."""
    if len(self) != len(other):          # relies on __len__ method
      raise ValueError('dimensions must agree')
    return self + other
    
  
  def __mul__(self, s):
    if isinstance(s, (int,float)):
      return [s* x for x in self]
    elif isinstance(s, (Vector)):
      return sum([x*y for x,y in zip(self,s)])  
    else:                                  
        raise TypeError('invalid parameter type')

  def __rmul__(self, s):
      return self * s
  

if __name__ == '__main__':
  # the following demonstrates usage of a few methods
  v = Vector(5)              # construct five-dimensional <0, 0, 0, 0, 0>
  v[1] = 23                  # <0, 23, 0, 0, 0> (based on use of __setitem__)
  v[-1] = 45  
  
  print(list(v))
  w = Vector(5)
  w[1] = 10
  w[2] = -5
  w[3] = 2
  w[4] = -15
  w[0] = 10
  print(list(v))
  print(list(w))
  x = v * w
  print(v * w)  # TypeError: unsupported operand type(s) for *: 'int' and 'Vector'
  print(list(v*3))
# R-2.15
# ---------------------------------------------------------------------------

# R-2.16
# ---------------------------------------------------------------------------

# R-2.17
# ---------------------------------------------------------------------------

# R-2.18
# ---------------------------------------------------------------------------

# R-2.19
# ---------------------------------------------------------------------------

# R-2.20
# ---------------------------------------------------------------------------

# R-2.21
# ---------------------------------------------------------------------------

# R-2.22
# ---------------------------------------------------------------------------
from abc import ABCMeta, abstractmethod           # need these definitions

class Sequence(metaclass=ABCMeta):
  """Our own version of collections.Sequence abstract base class."""

  @abstractmethod
  def __len__(self):
    """Return the length of the sequence."""

  @abstractmethod
  def __getitem__(self, j):
    """Return the element at index j of the sequence."""

  def __contains__(self, val):
    """Return True if val found in the sequence; False otherwise."""
    for j in range(len(self)):
      if self[j] == val:                          # found match
        return True
    return False

  def index(self, val):
    """Return leftmost index at which val is found (or raise ValueError)."""
    for j in range(len(self)):
      if self[j] == val:                          # leftmost match
        return j
    raise ValueError('value not in sequence')     # never found a match

  def count(self, val):
    """Return the number of elements equal to given value."""
    k = 0
    for j in range(len(self)):
      if self[j] == val:                          # found a match
        k += 1
    return k

  def __eq__(self, other):
    """Return the number of elements equal to given value."""
    if len(self) != len(other):
        raise ValueError('dimensions must agree')
    k = 0
    for j in range(len(self)):
        if self[j] == other[j]:                          # found a match
            k += 1
    return k == len(self)



# R-2.23
# ---------------------------------------------------------------------------


from abc import ABCMeta, abstractmethod           # need these definitions

class Sequence(metaclass=ABCMeta):
  """Our own version of collections.Sequence abstract base class."""

  @abstractmethod
  def __len__(self):
    """Return the length of the sequence."""

  @abstractmethod
  def __getitem__(self, j):
    """Return the element at index j of the sequence."""

  def __contains__(self, val):
    """Return True if val found in the sequence; False otherwise."""
    for j in range(len(self)):
      if self[j] == val:                          # found match
        return True
    return False

  def index(self, val):
    """Return leftmost index at which val is found (or raise ValueError)."""
    for j in range(len(self)):
      if self[j] == val:                          # leftmost match
        return j
    raise ValueError('value not in sequence')     # never found a match

  def count(self, val):
    """Return the number of elements equal to given value."""
    k = 0
    for j in range(len(self)):
      if self[j] == val:                          # found a match
        k += 1
    return k

  def __eq__(self, other):
    """Return the number of elements equal to given value."""
    if len(self) != len(other):
        raise ValueError('dimensions must agree')

    k = 0
    for j in range(len(self)):
        if self[j] == other[j]:                          # found a match
            k += 1
    return k == len(self)

  def __lt__(self, other):
    """Return the number of elements equal to given value."""
    if len(self) != len(other):
        raise ValueError('dimensions must agree')

    k = 0
    for j in range(len(self)):
        if self[j] < other[j]:                          # found a match
            k += 1
    return k == len(self)


if __name__ == '__main__':
    myS1 = []
    myS2 = []
    myS1.append(20)
    myS1.append(35)

    myS2.append(15)
    myS2.append(15)
    
    myS1 < myS2  # False
    
    
# C-2.24
# ---------------------------------------------------------------------------

# C-2.25
# ---------------------------------------------------------------------------


# import collections

class Vector:
  """Represent a vector in a multidimensional space."""

  def __init__(self, d):
    if isinstance(d, int):
      self._coords = [0] * d
    else:                                  
      try:                                     # we test if param is iterable
        self._coords = [val for val in d]
      except TypeError:
        raise TypeError('invalid parameter type')

  def __len__(self):
    """Return the dimension of the vector."""
    return len(self._coords)

  def __getitem__(self, j):
    """Return jth coordinate of vector."""
    return self._coords[j]

  def __setitem__(self, j, val):
    """Set jth coordinate of vector to given value."""
    self._coords[j] = val

  def __add__(self, other):
    """Return sum of two vectors."""
    if len(self) != len(other):          # relies on __len__ method
      raise ValueError('dimensions must agree')
    result = Vector(len(self))           # start with vector of zeros
    for j in range(len(self)):
      result[j] = self[j] + other[j]
    return result

  def __sub__(self, other):
    """Return diff of two vectors."""
    if len(self) != len(other):          # relies on __len__ method
      raise ValueError('dimensions must agree')
    result = Vector(len(self))           # start with vector of zeros
    for j in range(len(self)):
      result[j] = self[j] - other[j]
    return result

  def __neg__(self):
    """Return neg of the vector."""
    result = Vector(len(self))           # start with vector of zeros
    for j in range(len(self)):
      result[j] = -self[j]
    return result

  def __eq__(self, other):
    """Return True if vector has same coordinates as other."""
    return self._coords == other._coords

  def __ne__(self, other):
    """Return True if vector differs from other."""
    return not self == other             # rely on existing __eq__ definition

  def __str__(self):
    """Produce string representation of vector."""
    return '<' + str(self._coords)[1:-1] + '>'  # adapt list representation

#  def __neg__(self):
#    """Return copy of vector with all coordinates negated."""
#    result = Vector(len(self))           # start with vector of zeros
#    for j in range(len(self)):
#      result[j] = -self[j]
#    return result

  def __mul__(self, s):
    if isinstance(s, (int,float)):
      return [s* x for x in self]
    elif isinstance(s, (Vector)):
      return sum([x*y for x,y in zip(self,s)])  
    else:                                  
        raise TypeError('invalid parameter type')
  
  def __lt__(self, other):
    """Compare vectors based on lexicographical order."""
    if len(self) != len(other):
      raise ValueError('dimensions must agree')
    return self._coords < other._coords

  def __le__(self, other):
    """Compare vectors based on lexicographical order."""
    if len(self) != len(other):
      raise ValueError('dimensions must agree')
    return self._coords <= other._coords

if __name__ == '__main__':
  # the following demonstrates usage of a few methods
  v = Vector(5)              # construct five-dimensional <0, 0, 0, 0, 0>
  v[1] = 23                  # <0, 23, 0, 0, 0> (based on use of __setitem__)
  v[-1] = 45                 # <0, 23, 0, 0, 45> (also via __setitem__)
  print(v[4])                # print 45 (via __getitem__)
  u = v + v                  # <0, 46, 0, 0, 90> (via __add__)

  
  print(u)                   # print <0, 46, 0, 0, 90>
  print(v)                   # print <0, 23, 0, 0, 45>

  w= v - u
  print(w)                   # print <0, -23, 0, 0, -45>
  x= -v                      
  print (x)                  # print <0, -23, 0, 0, -45>
  total = 0
  for entry in v:            # implicit iteration via __len__ and __getitem__
    total += entry
  print(total)               #68

#45
#<0, 46, 0, 0, 90>
#68

if __name__ == '__main__':
  # the following demonstrates usage of a few methods
  v = Vector(5)              # construct five-dimensional <0, 0, 0, 0, 0>
  vfoo =Vector(['foo','foo','boo'])
  print(vfoo)

# C-2.26
# ---------------------------------------------------------------------------

class ReverseSequenceIterator:
  """A reverse iterator for any of Python's sequence types."""

  def __init__(self, sequence):
    """Create a reverse iterator for the given sequence."""
    self._seq = sequence          # keep a reference to the underlying data
    self._k = 0                  # will increment to 0 on first call to next

  def __next__(self):
    """Return the next element, or else raise StopIteration error."""
    self._k += -1                  # advance to next index
    if self._k >= -len(self._seq):
      return(self._seq[self._k])  # return the data element
    else:
      raise StopIteration()       # there are no more elements

  def __iter__(self):
    """By convention, an iterator must return itself as an iterator."""
    return self


if __name__ == '__main__':
  s2 = ReverseSequenceIterator([1,2,3])
  [s for s in s2]
  # out [3, 2, 1]
  
# C-2.27
# ---------------------------------------------------------------------------

# C-2.28
# ---------------------------------------------------------------------------
import os
print (os.getcwd())
os.chdir("E:\\CS Python\Python4AlgoDataStr")
os.chdir("GoodrichPython\ch02\ch02")
print (os.getcwd())

from credit_card import CreditCard

class PredatoryCreditCard(CreditCard):
  """An extension to CreditCard that compounds interest and fees."""
  
  def __init__(self, customer, bank, acnt, limit, apr, num_calls=0):
    """Create a new predatory credit card instance.

    The initial balance is zero.

    customer  the name of the customer (e.g., 'John Bowman')
    bank      the name of the bank (e.g., 'California Savings')
    acnt      the acount identifier (e.g., '5391 0375 9387 5309')
    limit     credit limit (measured in dollars)
    apr       annual percentage rate (e.g., 0.0825 for 8.25% APR)
    """
    super().__init__(customer, bank, acnt, limit)  # call super constructor
    self._apr = apr
    self._num_monthly_calls = num_calls

  def charge(self, price):
    """Charge given price to the card, assuming sufficient credit limit.

    Return True if charge was processed.
    Return False and assess $5 fee if charge is denied.
    """
    success = super().charge(price)          # call inherited method
    if not success:
      self._balance += 5                     # assess penalty
    self._num_monthly_calls += 1
    return success                           # caller expects return value

  def process_month(self):
    """Assess monthly interest on outstanding balance."""
    if self._balance > 0:
      # if positive balance, convert APR to monthly multiplicative factor
      monthly_factor = pow(1 + self._apr, 1/12)
      print("monthly_factor", monthly_factor)
      print("pre balance", self._balance)
      self._balance *= monthly_factor
      print("factor monthly balance", self._balance)
      if (self._num_monthly_calls) > 10 :
          #add $1 for each call in the month exceeding 10 calls
          self._balance += self._num_monthly_calls - 10
      print("factor monthly & num balance", self._balance)
      self._num_monthly_calls = 0

if __name__ == '__main__':
  cc=PredatoryCreditCard('John Bowman', 'California Savings',\
                           '5391 0375 9387 5309', 2500, 0.25) 

  cc.charge(3000)
  print('Customer =',cc.get_customer())
  print('Bank =', cc.get_bank())
  print('Account =', cc.get_account())
  print('Limit =', cc.get_limit())
  print('Balance =', cc.get_balance())
  print('New balance =', cc.get_balance())
  print()

  cc2=PredatoryCreditCard('John Bowman2', 'California Savings',\
                           '5391 0375 9387 5309', 2500, 0.25) 
  print(cc2.get_balance())
  for i in range(0,15):
    cc2.charge(100)
  cc2.process_month()
  
  print(cc2.get_balance())
  
  

# C-2.29
# ---------------------------------------------------------------------------

import os
print (os.getcwd())
os.chdir("E:\\CS Python\Python4AlgoDataStr")
os.chdir("GoodrichPython\ch02\ch02")
print (os.getcwd())

from credit_card import CreditCard

class PredatoryCreditCard(CreditCard):
  """An extension to CreditCard that compounds interest and fees."""
  
  def __init__(self, customer, bank, acnt, limit, apr, num_calls=0, factor=0.01):
    """Create a new predatory credit card instance.

    The initial balance is zero.

    customer  the name of the customer (e.g., 'John Bowman')
    bank      the name of the bank (e.g., 'California Savings')
    acnt      the acount identifier (e.g., '5391 0375 9387 5309')
    limit     credit limit (measured in dollars)
    apr       annual percentage rate (e.g., 0.0825 for 8.25% APR)
    """
    super().__init__(customer, bank, acnt, limit)  # call super constructor
    self._apr = apr
    self._num_monthly_calls = num_calls
    self._monthly_min = 0
    self._factor = factor

  def charge(self, price):
    """Charge given price to the card, assuming sufficient credit limit.

    Return True if charge was processed.
    Return False and assess $5 fee if charge is denied.
    """
    success = super().charge(price)          # call inherited method
    if not success:
      self._balance += 5                     # assess penalty
    else:
      self._monthly_min += self._factor * price  
    self._num_monthly_calls += 1
    
    
    return success                           # caller expects return value

  def make_payment(self, amount):
      super().make_payment(amount)
      self._monthly_min -= amount
      
  def process_month(self):
    """Assess monthly interest on outstanding balance."""
    late_fee = 10
    if self._balance > 0:
      # if positive balance, convert APR to monthly multiplicative factor
      monthly_factor = pow(1 + self._apr, 1/12)
      print("monthly_factor", monthly_factor)
      print("pre balance", self._balance)
      self._balance *= monthly_factor
      print("factor monthly balance", self._balance)
      if (self._num_monthly_calls) > 10 :
          #add $1 for each call in the month exceeding 10 calls
          self._balance += self._num_monthly_calls - 10
      print("factor monthly & num balance", self._balance)
      if self._monthly_min > 0 :
          self._balance += late_fee
          print("factor monthly & num balance & late fee", self._balance)
      self._num_monthly_calls = 0
      self._monthly_min = self._factor * self._balance

if __name__ == '__main__':
  cc=PredatoryCreditCard('John Bowman', 'California Savings',\
                           '5391 0375 9387 5309', 2500, 0.25) 

  cc.charge(3000)
  print('Customer =',cc.get_customer())
  print('Bank =', cc.get_bank())
  print('Account =', cc.get_account())
  print('Limit =', cc.get_limit())
  print('Balance =', cc.get_balance())
  print('New balance =', cc.get_balance())
  print()

  cc2=PredatoryCreditCard('John Bowman2', 'California Savings',\
                           '5391 0375 9387 5309', 2500, 0.25) 
  print(cc2.get_balance())
  for i in range(0,15):
    cc2.charge(100)
  cc2.process_month()
  
  print(cc2.get_balance())
  
  

# C-2.30
# ---------------------------------------------------------------------------

class CreditCard:
  """A consumer credit card."""
  
  def __init__(self, customer, bank, acnt, limit):
    """Create a new credit card instance.

    The initial balance is zero.

    customer  the name of the customer (e.g., 'John Bowman')
    bank      the name of the bank (e.g., 'California Savings')
    acnt      the acount identifier (e.g., '5391 0375 9387 5309')
    limit     credit limit (measured in dollars)
    """
    self._customer = customer
    self._bank = bank
    self._account = acnt
    self._limit = limit
    self._balance = 0

  def get_customer(self):
    """Return name of the customer."""
    return self._customer
    
  def get_bank(self):
    """Return the bank's name."""
    return self._bank

  def get_account(self):
    """Return the card identifying number (typically stored as a string)."""
    return self._account

  def get_limit(self):
    """Return current credit limit."""
    return self._limit

  def get_balance(self):
    """Return current balance."""
    return self._balance

  def _set_balance(self, amount):
      self._set_balance (amount)
      
  def charge(self, price):
    """Charge given price to the card, assuming sufficient credit limit.

    Return True if charge was processed; False if charge was denied.
    """
    if price + self._balance > self._limit:  # if charge would exceed limit,
      return False                           # cannot accept charge
    else:
      self._set_balance (self.get_balance() + price)
      return True

  def make_payment(self, amount):
    """Process customer payment that reduces balance."""
    self._set_balance (self.get_balance() - amount)



class PredatoryCreditCard(CreditCard):
  """An extension to CreditCard that compounds interest and fees."""
  
  def __init__(self, customer, bank, acnt, limit, apr):
    """Create a new predatory credit card instance.

    The initial balance is zero.

    customer  the name of the customer (e.g., 'John Bowman')
    bank      the name of the bank (e.g., 'California Savings')
    acnt      the acount identifier (e.g., '5391 0375 9387 5309')
    limit     credit limit (measured in dollars)
    apr       annual percentage rate (e.g., 0.0825 for 8.25% APR)
    """
    super().__init__(customer, bank, acnt, limit)  # call super constructor
    self._apr = apr

  def charge(self, price):
    """Charge given price to the card, assuming sufficient credit limit.

    Return True if charge was processed.
    Return False and assess $5 fee if charge is denied.
    """
    success = super().charge(price)          # call inherited method
    if not success:
      self._set_balance(self.get_balance() + 5)                     # assess penalty
    return success                           # caller expects return value

  def process_month(self):
    """Assess monthly interest on outstanding balance."""
    if self._balance > 0:
      # if positive balance, convert APR to monthly multiplicative factor
      monthly_factor = pow(1 + self._apr, 1/12)
      self._set_balance(self.get_balance() * (1+ monthly_factor))


# C-2.31
# ---------------------------------------------------------------------------
class Progression:
  """Iterator producing a generic progression.

  Default iterator produces the whole numbers 0, 1, 2, ...
  """

  def __init__(self, start=0):
    """Initialize current to the first value of the progression."""
    self._current = start

  def _advance(self):
    """Update self._current to a new value.

    This should be overridden by a subclass to customize progression.

    By convention, if current is set to None, this designates the
    end of a finite progression.
    """
    self._current += 1

  def __next__(self):
    """Return the next element, or else raise StopIteration error."""
    if self._current is None:    # our convention to end a progression
      raise StopIteration()
    else:
      answer = self._current     # record current value to return
      self._advance()            # advance to prepare for next time
      return answer              # return the answer

  def __iter__(self):
    """By convention, an iterator must return itself as an iterator."""
    return self                  

  def print_progression(self, n):
    """Print next n values of the progression."""
    print(' '.join(str(next(self)) for j in range(n)))

class ArithmeticProgression(Progression):  # inherit from Progression
  """Iterator producing an arithmetic progression."""
  
  def __init__(self, increment=1, start=0):
    """Create a new arithmetic progression.

    increment  the fixed constant to add to each term (default 1)
    start      the first term of the progression (default 0)
    """
    super().__init__(start)                # initialize base class
    self._increment = increment

  def _advance(self):                      # override inherited version
    """Update current value by adding the fixed increment."""
    self._current += self._increment

    
class GeometricProgression(Progression):   # inherit from Progression
  """Iterator producing a geometric progression."""
  
  def __init__(self, base=2, start=1):
    """Create a new geometric progression.

    base       the fixed constant multiplied to each term (default 2)
    start      the first term of the progression (default 1)
    """
    super().__init__(start)
    self._base = base

  def _advance(self):                      # override inherited version
    """Update current value by multiplying it by the base value."""
    self._current *= self._base


class FibonacciProgression(Progression):
  """Iterator producing a generalized Fibonacci progression."""
  
  def __init__(self, first=0, second=1):
    """Create a new fibonacci progression.

    first      the first term of the progression (default 0)
    second     the second term of the progression (default 1)
    """
    super().__init__(first)              # start progression at first
    self._prev = second - first          # fictitious value preceding the first

  def _advance(self):
    """Update current value by taking sum of previous two."""
    self._prev, self._current = self._current, self._prev + self._current

class DiffFibonacciProgression(Progression):
  """Iterator producing a generalized Fibonacci progression."""
  
  def __init__(self, first=2, second=200):
    """Create a new fibonacci progression.

    first      the first term of the progression (default 0)
    second     the second term of the progression (default 1)
    """
    super().__init__(first)              # start progression at first
    self._prev = second # abs(second - first)          # fictitious value preceding the first
    self._flag = -1

  def _advance(self):
    """Update current value by taking sum of previous two."""
    if self._flag == -1:
      self._prev, self._current = self._current, self._prev
      self._flag = 1
    else:
      self._prev, self._current = self._current, abs(self._prev - self._current)

if __name__ == "main":
  
  DiffFibonacciProgression().print_progression(10)

# C-2.32
# ---------------------------------------------------------------------------


class Progression:
  """Iterator producing a generic progression.

  Default iterator produces the whole numbers 0, 1, 2, ...
  """

  def __init__(self, start=0):
    """Initialize current to the first value of the progression."""
    self._current = start

  def _advance(self):
    """Update self._current to a new value.

    This should be overridden by a subclass to customize progression.

    By convention, if current is set to None, this designates the
    end of a finite progression.
    """
    self._current += 1

  def __next__(self):
    """Return the next element, or else raise StopIteration error."""
    if self._current is None:    # our convention to end a progression
      raise StopIteration()
    else:
      answer = self._current     # record current value to return
      self._advance()            # advance to prepare for next time
      return answer              # return the answer

  def __iter__(self):
    """By convention, an iterator must return itself as an iterator."""
    return self                  

  def print_progression(self, n):
    """Print next n values of the progression."""
    print(' '.join(str(next(self)) for j in range(n)))

class ArithmeticProgression(Progression):  # inherit from Progression
  """Iterator producing an arithmetic progression."""
  
  def __init__(self, increment=1, start=0):
    """Create a new arithmetic progression.

    increment  the fixed constant to add to each term (default 1)
    start      the first term of the progression (default 0)
    """
    super().__init__(start)                # initialize base class
    self._increment = increment

  def _advance(self):                      # override inherited version
    """Update current value by adding the fixed increment."""
    self._current += self._increment

    
class GeometricProgression(Progression):   # inherit from Progression
  """Iterator producing a geometric progression."""
  
  def __init__(self, base=2, start=1):
    """Create a new geometric progression.

    base       the fixed constant multiplied to each term (default 2)
    start      the first term of the progression (default 1)
    """
    super().__init__(start)
    self._base = base

  def _advance(self):                      # override inherited version
    """Update current value by multiplying it by the base value."""
    self._current *= self._base

class SquareRootProgression(Progression):
  """Iterator producing a geometric progression."""
  
  def __init__(self, root=2, start=65536):
    """Create a new square root progression.

    base       the fixed constant multiplied to each term (default 2)
    start      the first term of the progression (default 1)
    """
    super().__init__(start)
    self._root = root

  def _advance(self):                      # override inherited version
    """Update current value by multiplying it by the base value."""
    self._current =  self._current ** (1/self._root)
      
if __name__ == "main":
    SquareRootProgression().print_progression(10)
    