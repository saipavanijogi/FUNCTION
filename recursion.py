def function(n):
    if n==0:
        return 0
    return function(n-1)+n
n=int(input("enter the number"))
answer=function(n)
print(answer)