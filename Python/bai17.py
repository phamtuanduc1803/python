s=raw_input('Nhap vao : ')
d={'chuhoa':0,'chuthuong':0}
for c in s:
    if c.isupper():
        d['chuhoa']+=1
    if c.islower():
        d['chuthuong']+=1
print 'So chu hoa la : ',d['chuhoa'],'\n','So chu thuong la : ',d['chuthuong']
