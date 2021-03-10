#python Fibonacci sequence
#n1=1
#n2=1
#n3=n1+n2,n4=n3+n2...n13=n11+n12
#print(n13)

a=1
b=1
c=0
i=2
print(a)
print(b)
while i<13:
    c=a+b
    a=b
    b=c
    i=i+1
    print(c)
