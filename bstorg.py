class node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

class bst:
    def __init__(self):
        self.curnode=None
    
    def insert(self,val):
        if self.curnode==None:
            self.curnode=node(val)
        else:
            current=self.curnode
            while True:
                if val<=current.data:
                        if current.left==None:
                            current.left=node(val)
                            break
                        else:
                            current=current.left
                elif val>current.data:
                    if current.right==None:
                        current.right=node(val)
                        break
                    else:
                        current=current.right
                
    def inorder(self,node):
        if node==None:
            return
        else:
            self.inorder(node.left)
            print(node.data,end=" ")
            self.inorder(node.right)

    def preorder(self,node):
        if node==None:
            return
        else:
            print(node.data,end=" ")
            self.preorder(node.left)
            self.preorder(node.right)

    def postorder(self,node):
        if node==None:
            return
        else:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.data,end=" ")

    def search(self,node,key):
        if node==None:
            print("key not found")
            return
        if node.data==key:
            print("key is found")
            return
        if node.data>key:
            self.search(node.left,key)
        else:
            self.search(node.right,key)

    def display(self,cn):
        if self.curnode==None:
            print("List is empty")
        else:
            temp=cn
            print(temp.data,end=" ")
            if cn.left!=None:
                self.display(cn.left)
            if cn.right!=None:
                self.display(cn.right)
    
    def min(self,node):
        while node.left!=None:
            node=node.left
        return node
            

    def delete(self,node,key):
        if node==None:
            return node
        if key<node.data:
            node.left=self.delete(node.left,key)
        elif key>node.data:
            node.right=self.delete(node.right,key)
        else:
            if node.left==None:
                temp=node.right
                print("Deleted element: ",node.data)
                node=None
                return temp
            
            if node.right==None:
                temp=node.left
                print("Deleted element: ",node.data)
                node=None
                return temp
            
            temp=self.min(node.right)
            print("Deleted element: ",node.data," and from right sub tree,")
            node.data=temp.data
            node.right=self.delete(node.right,temp.data)
        return node


b=bst()
b.insert(6)
b.insert(9)
b.insert(5)
b.insert(2)
b.insert(8)
b.insert(15)
b.insert(24)
b.insert(14)
b.insert(7)
b.insert(8)
b.insert(5)
b.insert(2)
b.display(b.curnode)
print("")
b.postorder(b.curnode)
print("")
b.preorder(b.curnode)
print("")
b.inorder(b.curnode)
print("")
b.search(b.curnode,4)
print(b.min(b.curnode).data)
b.delete(b.curnode,15).data
b.inorder(b.curnode)