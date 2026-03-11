ans = 0
for i in range(1,2021):
    while i>0:
     if i % 10==2:
       ans+=1
     i= i // 10
print(ans)
