myList = [1,2,3,4]
B=[]
for i in myList:
    B.append(i)
A = [myList]*3
print(A)
myList[2]=45
print(A)
print(B)