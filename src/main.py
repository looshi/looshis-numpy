import numpy as np
import time

# Fill a specific array shape with zeros
a = np.zeros((3,4))
print(f"a = {a},     a shape = {a.shape}, a data type = {a.dtype}")

# Compare a naive dot product implementation vs. numpy's
def mydot(m, n):
  accum = 0
  for i in range(0, len(m)):
    accum = accum + m[i] * n[i]
  return accum

def numpy_dot(m,n):
  return np.dot(m,n)

def time_now():
  return time.time()

def big_array(val, amount):
  arr = []
  for i in range(0, 2**amount):
    arr.append(val)
  return arr

a = big_array(1, 24)
b = big_array(2, 24)

now = time_now()
print(f"mydot {mydot(a,b)}") # 8 seconds
print("mydot elapsed", time_now() - now)

now = time_now()
c = np.array(a)
d = np.array(b)
print("np.array elapsed", time_now() - now)

now = time_now()
print(f"numpy_dot {numpy_dot(c,d)}") # 0.0831 seconds
print("numpy_dot elapsed", time_now() - now)
