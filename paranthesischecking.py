def bracketcheck(inp):
    balanced=1
    s=[]
    for i in inp:
        if i=="(":
            s.append(i)
        else:
            if len(s)==0:
                balanced=0
            else:
                s.pop()
    if balanced==1 and len(s)==0:
        return True
    else:
        return False

a="()((())()"
print(bracketcheck(a))