X=(int)(raw_input('Nhap X : '))
Y=(int)(raw_input('Nhap Y : '))
array=[[0 for i in range(Y)] for j in range(X)]
for j in range(X):
    for i in range(Y):
        array[j][i]=i*j
print array
