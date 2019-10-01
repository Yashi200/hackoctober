a=0
b=1

x=int(input("enter a number"))
print (a)
print(b)

for i in range(0,x-2):
    c=a+b
    print (c)
    a=b
    b=c
