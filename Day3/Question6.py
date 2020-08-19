dic1= {
    'a' : 500 ,
    'b' : 5874 ,
    'c' : 560 ,
    'd' : 400 ,
    'e' : 5000 ,
    'f' : 20
}
n=3
def max_n(dic1,n):
    lis1 = list(dic1.values())
    lis2=[]
    lis1.sort()
    for i in range(1,n+1):
        lis2.append(str(lis1[-i]))
    print(lis2)

max_n(dic1 , 3)