m=[[1, 2, 3], [5, 4, 3], [2, 4, 8]]
print(max(m[0][2], m[1][2], m[2][2]))
print(max(m[1][0], m[1][1], m[1][2]))
#######################################
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
#################################

arr = [[2, 7, 6], [9, 4, 1], [4, 3, 0]]
n=3


print(arr)

for i in range(n):
  for j in range(n):
    print(arr[i][j], end = ' ')
    
  print()
SUM = float()

for i in range(len(arr)):
  for j in range(len(arr[i])):
    if i == j:
      SUM += float(arr[i][j])

print(SUM)

for row in arr:
  sum_row = sum(row)
  if sum_row != SUM:
    flag_1 = 0
  else:
    flag_1 = 1
  column = list()

  for element in row:
    column.append(element)

  print(row)
print(sum_row)

 


if sum(column) != SUM:
  flag_1 = 0
else:
  flag_2 = 1

print('Magic!') if flag_1 and flag_2 else print('Not a magic :(')

n = 3
arr = [[1, 3, 0], [3, 2, 6], [0, 6, 5]]

for i in range(n):
  for j in range(n):
    print(arr[i][j], end = ' ')
  print()

couple_count = (len(arr) ** 2 - len(arr)) / 2
count_validate = 0

for i in range(len(arr)):
  for j in range(i + 1, len(arr[i])):
    if arr[i][j] == arr[j][i]:
      count_validate += 1

print(couple_count)
print(count_validate)

if couple_count == count_validate:
  print('Symmentic')
else:
  print('Asymmetric')
  ##############################################################################
  from random import*
arr = [[1, 2, 3, 4], [5, 4, 3, 1]]
for i in arr:
  for j in i:
    print(j, end = ' ')
  print()

count=list()

for row in arr:
  sum_arr=sum(row)
  count.append(sum_arr)
  max_c=max(count)
  min_c=min(count)
  max_r=max(row)
print(count)
print(max_c)
print(min_c)
print(max_r)

n=int(input())
m=int(input())
arr=list()
for i in range(n):
    brr=list()
    for j in range(m):
        brr.append(float(input()))
    arr.append(brr)

print(arr)

for i in range(n):
  for j in range(m):
    print(arr[i][j], end = ' ')
  print()

her=list()
for i in range(n):
    for j in range(m):
        if arr[i][j] % 2 == 1:
            arr[i][j] =  1
        else:
            arr[i][j]= 0
    her_s=arr.append(her)
    
print(arr)

    
