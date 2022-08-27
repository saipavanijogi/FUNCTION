def function(a):
    i=0
    c=[]
    while i<len(a):
        if len(a[i])!=2:
            c.append(a[i])
        i=i+1
    return c
s=function(["one","two","oh","ok","three"])
print(s)


  