#Extended Euclidean Algorithm==GCD
a=int(input('Enter r1: '))
b=int(input('Enter r2: '))
r1=a
r2=b
s1=1
s2=0
t1=0
t2=1
while(r2>0):
    q=int(r1/r2)
    r=r1-q*r2
    r1=r2
    r2=r
    s=s1-q*s2
    s1=s2
    s2=s
    t=t1-q*t2
    t1=t2
    t2=t   
gcd=r1
print('GCD is: ', gcd)
