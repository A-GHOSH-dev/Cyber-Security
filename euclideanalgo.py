#Euclidean Algorithm==GCD

a=int(input('Enter r1: '))
b=int(input('Enter r2: '))

r1=a
r2=b

while(r2>0):
    q=int(r1/r2)
    r=r1-q*r2
    r1=r2
    r2=r
gcd=r1
print('GCD is: ', gcd)