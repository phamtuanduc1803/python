import re
x=raw_input("Nhap mat khau : ")
s=x.split(',')
thoaman=[]
for i in s:
    if len(i)<6 or len(i)>12:
        continue
    else:
        pass
    if not re.search(r"[a-z]",i):
        continue
    elif not re.search(r"[0-9]",i):
        continue
    elif not re.search(r"[A-Z]",i):
        continue
    elif not re.search(r"[@#$]",i):
        continue
    else:
        pass
    thoaman.append(i)
print ",".join(thoaman)
