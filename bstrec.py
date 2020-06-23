class node:
    def __init__(self,data=None):
        self.data=data
        self.left=None
        self.right=None

class bst:
    def __init__(self):
        self.curnode=None
        self.cn=None
    
    def insert(self,val):
        if self.curnode==None:
            self.curnode=node(val)
        else:
            if self.curnode==None:
                return node(val)
            if val<self.curnode.data:
                temp=self.curnode
                self.curnode=self.curnode.left
                self.curnode=self.insert(val)
                temp.left=self.curnode
                self.curnode=temp
            elif val>self.curnode.data:
                temp=self.curnode
                self.curnode=self.curnode.right
                self.curnode=self.insert(val)
                temp.right=self.curnode
                self.curnode=temp
        return self.curnode
        
    def display(self,cn):
            if cn==None:
                return
            else:
                self.display(cn.left)
                self.display(cn.right)
                print(cn.data,end=" ")

b=bst()
b.insert(4)
b.insert(2)
b.insert(5)
b.insert(1)
b.display(b.curnode)