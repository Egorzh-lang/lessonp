n = int(input())
s = 0
for i in range(n+1):
    s = i*i*i + s 
print(s)
###################################

for i in range(1, 10):
    print(f"{i}|", end="")  
    for j in range(1, 10):
        if j*i > 9:
            print(f"  {i * j}", end="")
        else:
            print(f"   {i+j}", end="")  
