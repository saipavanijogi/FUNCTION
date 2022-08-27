def function(n):
    i=0
    a=[]
    while i<len(n):
        if n[i] not in a:
            a.append(n[i])
        i=i+1
    print(a)
function([1,2,3,3,3,3,4,5,6])

