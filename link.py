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
    
    def delete(self):
        if self.last==None:
            print("cannot delete at empty linked list")
        elif self.first==self.last:
            self.first=None
            self.last=None
        else:
            self.first=self.first.next

    def insertpos(self,item,i):
        if i==0:
            temp=self.first
            self.first=node(item)
            self.first.next=temp
        else:
            temp=self.first
            k=0
            while temp !=None:
                if k==i-1:
                    uk=temp.next
                    temp.next=node(item,uk)
                    break
                k=k+1
                temp=temp.next
            if k<i:
                    self.last.next=node(item)
                    self.last=self.last.next
    
    def delpos(self,i):
        temp=self.first
        if i==0:
            self.first=temp.next
            temp=None
        else:
            k=0
            while temp!=None:
                if k==i-1:
                    t=temp.next
                    temp.next=t.next
                    break
                k=k+1
                temp=temp.next

    def display(self):
        if self.first!=None:
            temp=self.first
            print("--",end="")
            while temp != None:
                print(temp.disn(),end="--")
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
l.display()
l.insertpos(13,0)
l.display()
l.delete()
l.display()
l.insertpos(14,3)
l.display()
l.delpos(1)
l.display()