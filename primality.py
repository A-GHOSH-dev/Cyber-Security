
# If n is a prime number, then for every a, 1 < a < n-1,

# an-1 ≡ 1 (mod n)
#  OR 
# an-1 % n = 1 
 

# Example: Since 5 is prime, 24 ≡ 1 (mod 5) [or 24%5 = 1],
#          34 ≡ 1 (mod 5) and 44 ≡ 1 (mod 5) 

#          Since 7 is prime, 26 ≡ 1 (mod 7),
#          36 ≡ 1 (mod 7), 46 ≡ 1 (mod 7) 
#          56 ≡ 1 (mod 7) and 66 ≡ 1 (mod 7) 

n=int(input('Enter n: '))
a=2 
while(n>0 and n%2!=0 and a<(n-1)):
    if((a^(n-1)) % n == 1):
        print("True")
        a=a+1
    else:
        print('not prime')

    
        
        