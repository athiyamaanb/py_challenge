x=set()
print(type(x))
list=[1,2,2,3,4,5,5,6]
for i in list:
   if  i not in x:
    x.add(i)
print(x)