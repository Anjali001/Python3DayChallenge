import sys
def divisible(x,y):
    for i in range(x,y+1):
        if i % 2 == 0:
            if i % 3 != 0:
                if i != y:
                    print(i,end=",")
                else:
                    print(i)

x=int(sys.argv[1])
y=int(sys.argv[2])
divisible(x,y)
