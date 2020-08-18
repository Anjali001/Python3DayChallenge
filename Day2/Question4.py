num = int(input("Enter a number"))
totprime=[]
for i in range(1,num+1):
    count=0
    for j in range(1,i+1):
        if i%j==0:
            count+=1
    if count == 2:
        totprime.append(i)

nub=num
prime_factors=[]
i = totprime[0]
while nub > 1:

    if nub % i == 0:
        prime_factors.append(i)
        nub /= i
        i=i-1
    i=i+1
print(prime_factors)

print(f'prime_factors({num})-->{prime_factors}')


        





    
