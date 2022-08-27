def fun():
    i=1
    l=[]
    while i<=6:
        n=int(input("enter the number"))
        l.append(n)
        i=i+1
    print(l)
# s=fun()
# print(s)
def evenodd(list):
    j=0
    while j<len(list):
        if list[j]%2==0:
            print("even")
        else:
            print("odd")
        j=j+1
evenodd(fun())
                
#     print(l)
# fun()
        
    