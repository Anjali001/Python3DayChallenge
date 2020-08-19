def Split_list(listt,num):
    list1=[]
    list2=[]
    for i,j in enumerate(listt):
        if i < num:
            list1.append(j)
        else:
            list2.append(j)
    if list1 != [] and list2 != []:
        print(f'{list1},{list2}')
    else:
        print(f'{list1}')

Split_list(['a','b','c','d','e','f','g','h','i','k'],3)
Split_list([],5)




