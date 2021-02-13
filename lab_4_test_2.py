def poluchilos(a):
  m=1
  for i in range(0,len(a),1):
    m=m*a[i]
  return m
print(poluchilos([5,10,2]))  