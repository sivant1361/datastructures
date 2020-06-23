arr=[1,2,3,4,5,9,7,6]
print("Initial array:",end=" ")
for i in arr:
    print(i,end=" ")
length=len(arr)
for i in range(1,length):
    data=arr[i]
    j=i-1
    while j>=0:
        if arr[j]>data:
            arr[j+1]=arr[j]
        else:
            break
        j=j-1
    arr[j+1]=data
print("")
print("Sorted array:",end=" ")
for i in arr:
    print(i,end=" ")