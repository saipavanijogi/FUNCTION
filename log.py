
list=[10,20,10,30,50,20,30,10,10]
i=0
c=[]
while i<len(list):
    a=list[i]
    list.remove(a)
    if a in list:
        b=a,a
        c.append(b)
    i=i+1
print(len(c))


