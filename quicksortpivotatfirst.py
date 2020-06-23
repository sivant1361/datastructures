def partision(arr,low,high):
    temp=arr[low]
    i=low
    for j in range(low+1,high+1):
        if arr[j]<temp:
            i=i+1
            arr[j],arr[i]=arr[i],arr[j]
    arr[low],arr[i]=arr[i],arr[low]
    return i

def quick(arr,low,high):
    if high>low:
        pi=partision(arr,low,high)
        quick(arr,low,pi-1)
        quick(arr,pi+1,high)
        

l=[3,6,5,4,1,2,8,7,10,9]
n=len(l)
quick(l,0,n-1)
for i in l:
    print(i,end=" ")