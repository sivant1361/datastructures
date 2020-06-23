class node:

    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next
    
    def disn(self):
        return self.data

class stack:
    def __init__(self):
        self.top=None
    
    def ins(self,val):
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
    
    def delete(self):
        if self.top !=None:
            if self.top.next==None:
                self.top=None
            else:
                temp=self.top
                self.top=temp.next
                temp=None
        else:
            print("Cannot pop for empty list")

s=stack()
s.ins(1)
s.ins(2)
s.ins(3)
s.ins(4)
s.display()
s.delete()
s.display()