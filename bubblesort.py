arr=[1,3,6,5,4,9,8,2]
lenght=len(arr)
for i in range(lenght):
    for j in range(lenght-i-1):
        if(arr[j]>arr[j+1]):
            arr[j+1],arr[j]=arr[j],arr[j+1]

for i in range(lenght):
    print(arr[i],end=" ") 