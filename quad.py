import math as m

class node:

    def __init__(self,data):
        self.data=data
        self.next=None

class quad:

    def __init__(self):
        self.eqn=None
        self.top=None
        self.dis=None

    def insert(self,val):
        if self.eqn==None:
            self.eqn=node(val)
            self.top=self.eqn
        else:
            self.eqn.next=node(val)
            self.eqn=self.eqn.next
    
    def quadobj(self,a,b,c):
        self.insert(a)
        self.insert(b)
        self.insert(c)
    
    def display(self):
        temp=self.top
        if temp==None:
            print("List is Empty!")
        else:
            print("The coefficient of x^2,x and contants are:")
            while temp!=None:
                print(temp.data,end=" ")
                temp=temp.next
                
    def discri(self):
        temp=self.top
        self.dis=pow(temp.next.data,2)-(4*temp.data*temp.next.next.data)
    
    def root(self):
        temp=self.top
        self.discri()
        if self.dis<0:
            print("No real root exist")
        if self.dis==0:
            r=(-temp.next.data)/(2*temp.data)
            print("The roots of the equation are: ",r)
        else:
            d=m.sqrt(self.dis)
            r1=((-temp.next.data)+d)/(2*temp.data)
            r2=((-temp.next.data)-d)/(2*temp.data)
            print("The roots of the equation are: ",r1," ",r2)

q=quad()
a=int(input("Enter coefficient of x^2:"))
b=int(input("Enter coefficient of x:"))
c=int(input("Enter coefficient of constant:"))
q.quadobj(a,b,c)
q.display()
print("")
q.root()
