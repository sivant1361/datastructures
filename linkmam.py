class node:
    def __init__(self,data):
        self.data=data
        self.next=None

class linklist:
    def __init__(self):
        self.head=None
        self.last=None

    def append(self,data):
        if self.head==None:
            self.head=node(data)
            self.last=self.head
        else:
            self.last.next=node(data)
            self.last=self.last.next