def primitiveRoots(k):
  for i in range(2, k):
    for j in range(1, k-1):
      if i**j % k == 1:
        break
    else:
      yield i

def makePoly(f, d=None, k=None):
  if d is None:
    d = 0
  if k is None:
    k = len(f)
  p = [0]*len(f)
  
  p[0] = f[-d % k]
  
  for j in range(1, k-1):
    s = 0
    for i in range(1, k):
      s += i**(k-1-j)*f[i-d]
    p[j] = -s % k
  
  p[k-1] = -1 * sum(f) % k
  
  return p

while True:
  s = input("Enter k to see primitive roots: ")
  if s.isdigit():
    print(*primitiveRoots(int(s)))
  f = [int(c) for c in input("Enter vector:\n").split(',')]
  k = len(f)
  for d in range(k):
    print("d={} p={}".format(d, makePoly(f, d, k)))
  print()
