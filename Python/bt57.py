s=str(input())
def format(s):
    if len(s)>2:
        if s[-3:]=="ing":
            print(s+"ly")
        else:
            print(s+"ing")
    else:
        print(s)
format(s)
