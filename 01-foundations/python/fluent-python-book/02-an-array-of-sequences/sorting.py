fruits = ['grape', 'raspberry', 'apple', 'banana']
print( sorted(fruits) )
fruits.sort()
print( fruits )

import bisect
HAYSTACK = [1, 4, 5, 6, 8, 12, 15, 20, 21, 23, 23, 26, 29, 30]

index = bisect.bisect(HAYSTACK, 20)
bisect.insort( HAYSTACK, 20)
print(index)
print(HAYSTACK)
