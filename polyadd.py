import math as m

class node:

    def __init__(self,data):
        self.data=data
        self.next=None

class poly:

    def __init__(self):
        self.top=None
    
    def insert(self,val):
        if self.top==None:
            self.top=node(val)
        else:
            temp=self.top
            self.top=node(val)
            self.top.next=temp
    
    def displaystr(self):
        temp=self.top
        if temp==None:
            print("List is Empty!")
        else:
            print("The coefficient of the resulting polynomial equation are:")
            while temp!=None:
                print(temp.data,end=" ")
                temp=temp.next
            return
        print("")
    
    def display(self,d3):
        temp=self.top
        if temp==None:
            print("List is Empty!")
        else:
            print("The coefficient of the resulting polynomial equation are:")
            while temp!=None:
                if d3>=1:    
                    print(temp.data,"x^"+str(d3),end=" ")
                    temp=temp.next
                    d3=d3-1
                else:
                    print(temp.data,end=" ")
                    temp=temp.next
            return
        print("")

p1=poly()
p2=poly()

d1=int(input("Enter number degree of the equation 1:"))
for i in range(d1+1,0,-1):
    if i!=1:
        p1.insert(int(input("Enter coefficient of x^"+str(i-1)+" :")))
    else:
        p1.insert(int(input("Enter coefficient of constant :")))
print("")
print("")

d2=int(input("Enter number degree of the equation 2:"))
for i in range(d2+1,0,-1):
    if i!=1:
        p2.insert(int(input("Enter coefficient of x^"+str(i-1)+" :")))
    else:
        p2.insert(int(input("Enter coefficient of constant :")))
print("")
print("")

p3=poly()
d3=0

if d1>d2:
    d3=d1
else:
    d3=d2

t1=p1.top
t2=p2.top
for i in range (d3+1):
    if t1!=None and t2!=None:
        p3.insert(t1.data+t2.data)
        t1=t1.next
        t2=t2.next
    else:
        if t1!=None:
            p3.insert(t1.data)
            t1=t1.next
        if t2!=None:
            p3.insert(t2.data)
            t2=t2.next

p3.display(d3)