# get and initiallize the values from user
n=int(input("enter a term to be displayed :  \n"))
a = 0
b = 1

#process the value
if n == 1:
    print(a)
else:
    print(a)
    print(b)
    for i in range(2,n):
        c = a + b
        a = b
        b = c
        print(c)
