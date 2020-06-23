def bs(arr,item):
    if len(arr)==0:
        print("Item not found")
    else:
        m=len(arr)//2
        if arr[m]==item:
            print("Item found at position:",m)
            return
        elif arr[m]<item:
            bs(arr[m+1:],item)
        else:
            bs(arr[:m],item)
            

arr=[1,2,3,4,5,6,7]
item=int(input("Enter the element to be found:"))
bs(arr,item)