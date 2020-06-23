class node:

    def __init__(self,data):
        self.data=data
        self.next=None

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
        else:
            if self.last.next==self.last:
                temp=self.front
                self.front=None
                self.last=None
            else:
                temp=self.front
                self.front=self.front.next
            print("Deleted element: ",temp.data)
            temp=None

    def display(self):
        if self.front!=None:
            temp=node(None)
            temp=self.front
            while temp != None:
                print(temp.data,end=" ")
                temp=temp.next
            print("")
        else:
            print("can't print empty list")

l=queue()
l.enqueue(1)
l.enqueue(3)
l.enqueue(6)
l.enqueue(0)
l.enqueue(1)
print("Queue: ",end=" ")
l.display()
l.dequeue()
print("Queue after deletion: ",end=" ")
l.display()