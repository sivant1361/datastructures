arr=[1,3,5,6,4,2,8,7]
l=len(arr)
for i in range(l):
    for j in range(i+1,l):
        if arr[j]<arr[i]:
            arr[j],arr[i]=arr[i],arr[j]

for i in arr:
    print(i,end=" ")
