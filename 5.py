def function( a):
    i=0
    o=[]
    while i<len(a):
        if a[i]!="remove":
            o.append(a[i])
        i=i+1
    return o
s=function(["sushama","pavani","remove","remove","bujjuodu"])
print(s)


    