m=[[1, 2, 3], [5, 4, 3], [2, 4, 8]]
print(max(m[0][2], m[1][2], m[2][2]))
print(max(m[1][0], m[1][1], m[1][2]))

import random

n=int(input())
m=int(input())
arr=list()
for i in range(n):
  row=list()
  for j in range(m):
    row.append(float(round(random.randint(0, 100))))
arr.append(row)



print(arr)
