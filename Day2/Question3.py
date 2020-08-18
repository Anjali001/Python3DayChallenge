def fact(x):
    prod = 1
    while x>=1:
        prod *= x
        x-=1
    return prod

num = int(input("Enter The number : "))
print(f'factorial of {num} is ',fact(num))