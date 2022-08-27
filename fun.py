def primeorNot(num):
    i=0
    j=0
    a=num%2
    while i<=a:
        if num%i==0:
            j=1
            break
        i=i+1
    if j==0:
        print("is not a prime number")
    else:
        print("it is not prime number")
primeorNot(406)

