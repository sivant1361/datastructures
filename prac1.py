class node:

    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next

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
    
    def delete(self):
        if self.last==None:
            print("cannot delete at empty linked list")
        else:
            if self.last.next==self.last:
                temp=self.first
                self.first=None
                self.last=None
            else:
                temp=self.first
                self.first=self.first.next
            print("Deleted element: ",temp.data)
            temp=None

    def display(self):
        if self.first!=None:
            temp=node(None)
            temp=self.first
            while temp != None:
                print(temp.data,end=" ")
                temp=temp.next
            print("")
        else:
            print("can't print empty list")

l=linlis()
l.insert(1)
l.insert(4)
l.insert(3)
l.insert(2)
l.insert(6)
print("Linked list: ",end=" ")
l.display()
l.delete()
print("Linked List after deletion: ",end=" ")
l.display()