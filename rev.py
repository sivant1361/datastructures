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
            no=node(n)
            self.last.next=no
            self.last=self.last.next
            
    def delete(self):
        if self.last==None:
            print("cannot delete at empty linked list")
        elif self.last.next==self.last:
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
                    t=temp
                    temp=temp.next
                    t.next=temp.next
                    break
                k=k+1
                temp=temp.next

    def display(self):
        if self.first!=None:
            temp=node(None)
            temp=self.first
            print("--",end="")
            while temp != None:
                print(temp.disn(),end="--")
                temp=temp.next
            print("")
        else:
            print("can't print empty list")

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

def rev(l):
    s=stack()
    temp=l.first
    while temp!=None:
        s.ins(temp.data)
        temp=temp.next
    s.display()
    print("")
    return s

def pallindrome(l,s):
    t1=l.first
    t2=s.top
    while t1!=None:
        if t1.data!=t2.data:
            print("It is not a pallindrome!!!")
            return
        t1=t1.next
        t2=t2.next
    else:
        print("It is a pallindrome")

l=linlis()

# l.insert(1)
# l.insert(4)
# l.insert(3)
# l.insert(2)
# l.insert(5)
# l.insert(6)

l.insert(1)
l.insert(3)
l.insert(3)
l.insert(1)

l.display()
s=rev(l)
pallindrome(l,s)
