numbers = [3, 5, 7, 34, 2, 89, 2, 5]
# o/p 89
def function(list):
    i=0
    max=0
    while i<len(list):
        if list[i]>max:
            max=(list[i])
        i=i+1
    print(max)
function([3, 5, 7, 34, 2, 89, 2, 5])

