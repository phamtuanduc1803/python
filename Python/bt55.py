str="pham tuan duc a as asd"
def bt55(str):
    lst1=[]
    lst=str.split()
    for s in lst:
        if len(s)>=3:
            lst1.append(s)
    print(lst1)
bt55(str)
