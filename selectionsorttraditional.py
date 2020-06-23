import time
t=time.time()
arr=[1,3,5,6,4,2,8,7]

l=len(arr)
for i in range(l):
    s=arr[i]
    index=i
    for j in range(i+1,l):
        if arr[j]<s:
            s=arr[j]
            index=j
    arr[i],arr[index]=arr[index],arr[i]
    
for i in arr:
    print(i,end=" ")
print(" ")
print((time.time()-t))