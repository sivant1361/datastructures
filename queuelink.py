class node:

    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next
    
    def disn(self):
        return self.data

class queue:

    def __init__(self):
        self.front=None
        self.last=None

    def enqueue(self,n):
        if self.front is None:
            self.front=node(n)
            self.last=self.front
        else:
            self.last.next=node(n)
            self.last=self.last.next
    
    def dequeue(self):
        if self.last==None:
            print("cannot delete at empty linked list")
        elif self.last.next==self.last:
            self.front=None
            self.last=None
        else:
            self.front=self.front.next

    def display(self):
        if self.front!=None:
            temp=node(None)
            temp=self.front
            while temp != None:
                print(temp.disn(),end=" ")
                temp=temp.next
            print("")
        else:
            print("can't print empty list")

l=queue()
l.enqueue(7)
l.enqueue(1)
l.enqueue(3)
l.enqueue(0)
l.enqueue(6)
l.enqueue(0)
l.enqueue(1)
l.display()
l.dequeue()
l.display()