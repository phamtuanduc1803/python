s=raw_input('Nhap vao : ')
d={'chu':0,'so':0}
for c in s:
    if c.isdigit():
        d['so']+=1
    if c.isalpha():
        d['chu']+=1
print 'So chu cai la : ',d['chu']
print 'So chu so la : ',d['so']
