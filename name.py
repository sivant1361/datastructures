import array as ar
a=ar.array("u",["s","i","v","a"])
print(a)
a.insert(4,"n")
a.insert(5,"t")
a.remove("s")
print(a)
print(a.index("v"))