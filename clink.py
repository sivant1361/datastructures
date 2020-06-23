class node:

    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next
    
    def disn(self):
        return self.data

class linlis:

    def __init__(self):
        self.first=None
        self.last=None

    def insert(self,n):
        if self.first is None:
            self.first=node(n)
            self.last=self.first
        else:
            self.last.next=node(n)
            self.last=self.last.next
            self.last.next=self.first
    
    def delete(self):
        if self.last==None:
            print("cannot delete at empty linked list")
        elif self.last.next==self.last:
            self.first=None
            self.last=None
        else:
            temp=self.first
            self.first=temp.next
            temp=None
            self.last.next=self.first

    def display(self):
        if self.first.next==None:
            print("--",self.first.data,"--")
        elif self.first!=None:
            temp=self.first
            print("--",end="")
            while temp.next!=None:
                print(temp.disn(),end="--")
                if temp.next==self.first:
                    break
                temp=temp.next
            print("")
        else:
            print("can't print empty list")

l=linlis()
l.insert(1)
l.insert(4)
l.insert(3)
l.insert(2)
l.insert(5)
l.insert(6)
print("Linked list: ",end=" ")
l.display()
l.delete()
print("Linked List after deletion: ",end=" ")
l.display()