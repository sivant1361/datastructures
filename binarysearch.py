arr=[1,2,3,4,5,6,7]
item=int(input("Enter the element to be found:"))
flag=0
f=0
e=len(arr)
m=int((f+e)/2)
while f<e:
    if arr[m]==item:
        print("Item found at position:",m)
        flag=1
        break
    elif arr[m]<item:
        f=m+1
    if arr[m]>item:
        e=m-1
    m=int((f+e)/2)
if flag==0:
        print("Item not found")