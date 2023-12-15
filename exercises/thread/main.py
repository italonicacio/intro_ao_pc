from threading import Thread
import sys
import numpy as np

def LinearSearch(arr, r):
    max_ = -sys.maxsize - 1
    for e in arr:
        if e > max_:
            max_ = e

    r[0] = max_


# v = np.random.randint(low=0,high=100000000, size=1000000)
v = np.random.randint(low=0,high=100000000, size=1000000000)


arr1 = v[0:len(v)//2]
r1 = [0]

arr2 = v[len(v)//2:len(v)]
r2 = [0]

t = Thread(target=LinearSearch, args=(arr1, r1))

t.start()
LinearSearch(arr2, r2)

t.join()

print(r1)
print(r2)


