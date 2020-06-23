arr=[9,2,5,6,4,7,8,3]
length=len(arr)
for i in range(1,length):
    data=arr[i]
    j=i-1
    while j>=0 and arr[j]>data:
        arr[j+1]=arr[j]
        j=j-1
    arr[j+1]=data
print(arr)