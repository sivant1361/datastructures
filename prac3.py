class node:

    def __init__(self,data):
        self.data=data
        self.next=None

class stack:
    def __init__(self):
        self.top=None
    
    def push(self,val):
        if self.top==None:
            self.top=node(val)
        else:
            temp=self.top
            self.top=node(val)
            self.top.next=temp
    
    def display(self):
        temp=self.top
        while temp!=None:
            print(temp.data,end=" ")
            temp=temp.next
        print("")
    
    def pop(self):
        if self.top !=None:
            if self.top.next==None:
                temp=self.top
                self.top=None
            else:
                temp=self.top
                self.top=temp.next
            print("poped element: ",temp.data)
            temp=None
        else:
            print("Cannot pop for empty list")

s=stack()
s.push(1)
s.push(2)
s.push(3)
s.push(4)
print("Stack: ",end=" ")
s.display()
s.pop()
print("Stack after deletion: ",end=" ")
s.display()