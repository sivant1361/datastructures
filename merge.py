l1=[1,3,4,5,7]
l2=[2,4,6,8,10]
l3=[]
i=0
j=0
a=int(len(l1))
b=int(len(l2))

while i<a and j<b:
    if l1[i]>l2[j]:
        l3.append(l2[j])
        j+=1
    else:
        l3.append(l1[i])
        i+=1

while i<a:
    l3.append(l2[i])
    i=i+1

while j<b:
    l3.append(l2[j])
    j=j+1

print(l3)