def function(p):
    i=0
    a=[]
    b=[]
    while i<len(p):
        c=p.count(p[i])
        d=p[i],c
        a.append(d)
        i=i+1
    return a
s=function("massiccipi")
print(s)

