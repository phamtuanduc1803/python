sum=0
while True:
    s=raw_input()
    if not s:
        break
    x=s.split(' ')
    if x[0] == 'D':
        sum += int(x[1])
    if x[0] == 'W':
        sum -= int(x[1])
print 'Tai khoan con : ',sum
