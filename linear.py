a=[-23,97,18,21,5,-86,64,0,-37]
item=int(input("Enter element to be found:"))
flag=0
for i in range(len(a)):
    if item == a[i]:
        print("Item found at index:",i)
        flag=1
        break
if flag==0:
    print("Item not found")
    