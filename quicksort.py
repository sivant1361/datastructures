def partision(arr,low,high):
    pivot=arr[high]
    i=low-1
    for j in range(low,high):
        if arr[j]<pivot:
            i=i+1
            arr[j],arr[i]=arr[i],arr[j]
    arr[high],arr[i+1]=arr[i+1],arr[high]
    return i+1

def quick(arr,low,high):
    if high>low:
        pi=partision(arr,low,high)
        quick(arr,low,pi-1)
        quick(arr,pi+1,high)

l=[1,3,6,4,2,5]
n=len(l)
quick(l,0,n-1)
for i in l:
    print(i,end=" ")