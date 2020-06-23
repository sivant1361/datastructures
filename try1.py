import array as arr

a=arr.array('i',[1,2,3])
a.insert(12,15)
print(a)

b=arr.array("d",[10.24,10.54,67.34,99.43])
b.insert(4,42.67)
b.insert(5,78.42)
print(b)
b.remove(10.54)
print(b.index(67.34))
print(b)