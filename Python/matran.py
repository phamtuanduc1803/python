def chessBoardCellColor(cell1,cell2):
    return (ord(cell1[0])+int(cell1[1]))%2==(ord(cell2[0])+int(cell2[1]))%2

def bishopAndPawn(bishop,pawn):
    if bishop==pawn:
        return False
    return abs((ord(bishop[0])-ord(pawn[0])))==abs(int(bishop[1])-int(pawn[1]))
               
def spiralNumbers(n):
    arr=[]
    for i in range(0,n):
        a=[0]*n
        arr.append(a)
    i=0
    j=0
    k=n-1
    c=1
    while c<n*n:
        while j<k:
            arr[i][j]+=c
            c+=1
            j+=1
        while i<k:
            arr[i][j]+=c
            c+=1
            i+=1
        while j>(n-1-k):
            arr[i][j]+=c
            c+=1
            j-=1
        while i>(n-k):
            arr[i][j]+=c
            c+=1
            i-=1
        k-=1
    arr[i][j]=n*n
    return arr

def checkingSudoku(grid):
    cols=len(grid[0])
    rows=len(grid)
    for i in range(0,rows):
        for j in range(0,cols):
            if '1'<=grid[i][j]<='9':
                if grid[i][j] in grid[i][j+1:]:
                    return False
                for k in range(i+1,rows):
                    if grid[i][j]==grid[k][j]:
                        return False
                a=int(i/3)
                b=int(j/3)
                
                for x in range(a*3,a*3+3):
                    for y in range(b*3,b*3+3):
                        if x==i and y==j:
                            continue
                        if grid[i][j]==grid[a][b]:
                            return False
    return True

def findPath(matrix):
    x=0
    y=0
    for i in range(0,len(matrix)):
        for j in range(0,len(matrix[0])):
            if matrix[i][j]==1:
                x=i
                y=j
                break
        if matrix[x][y]==1:
            break
    while True:
        if x-1>=0 and matrix[x-1][y]==matrix[x][y]+1:
            x-=1
            continue
        if x+1<len(matrix) and matrix[x+1][y]==matrix[x][y]+1:
            x+=1
            continue
        if y-1>=0 and matrix[x][y-1]==matrix[x][y]+1:
            y-=1
            continue
        if y+1<len(matrix[0]) and matrix[x][y+1]==matrix[x][y]+1:
            y+=1
            continue
        break
    if matrix[x][y]==len(matrix)*len(matrix[0]):
        return True
    else:
        return False
arr= [[1,2,3],   [6,5,4],   [7,8,9],   [12,11,10]]

print(findPath(arr))







