import time
from array import array
import sys
from random import random

### Array

lista = [random() for i in range(10**7)]
print("List Total time => ", sys.getsizeof(lista))

floats = array('d', ( random() for i in range(10**7)))
print("Array Total time => ", sys.getsizeof(floats))

### Memory views

octest = array('B', range(6))
print(octest)

m1 = memoryview(octest)
m1.tolist()
print(m1)

m2 = m1.cast('B', [2,3])
print(m2)
print( m2.tolist() )

m3 = m1.cast('B', [3,2])
print(m3)
print(m3.tolist())

m2[1,1] = 22
m3[1,1,] = 33
print( octest )

#### Numpy

import numpy as np

a = np.arange(12)
type(a)

a.shape = 3,4

### Deque

from collections import deque

dq = deque(range(10), maxlen=10)
dq.rotate(3)
dq.rotate(-4)
dq.appendleft(-1)
dq.extend([11,22,33])
dq.extendleft([10,20,30,40,50])

