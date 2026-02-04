a=[1,1,2,2,2,2,3,4,4,5,5,5,6]
i=0
for j in range(1,len(a)):
    if a[i]!=a[j]:
        i+=1
        a[i]=a[j]

k=i+1
print(a)
print("k=",k)
