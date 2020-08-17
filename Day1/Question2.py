def number(a):
    count = 0
    for i in a:
        if i !=0:
            count+=1
    print(f'number of elements in list {listt} are:{count}')

listt =[]
x=0
while x==0:
    a=input("Enter the element")
    listt.append(a)
    x =int(input("0 for entering more and 1 to stop entering"))

number(listt)