import sys
def rook(arr):
    visit=[]
    queue=[]
    for i in range(0,len(arr)):
        for j in range(0,len(arr[0])):
            if arr[i][j]=='s':
                si=i
                sj=j
    if sj-1>=0 and arr[si][sj-1]!='#':
      queue.append([si,sj-1,1,1])
    if sj+1<len(arr[0]) and arr[si][sj+1]!='#':
        queue.append([si,sj+1,2,1])
    if si-1>=0 and arr[si-1][sj]!='#':
        queue.append([si-1,sj,3,1])
    if si+1<len(arr) and arr[si+1][sj]!='#':
        queue.append([si+1,sj,4,1])
    while len(queue)!=0:
        i=queue[0][0]
        j=queue[0][1]
        huong=queue[0][2]
        count=queue[0][3]
        queue.pop(0)
        if [i,j,huong] in visit:
            continue
        visit.append([i,j,huong])
        if huong==1:
            while j>=0 and arr[i][j]!='#' and arr[i][j]!='s':
                if arr[i][j]=='g':
                    return count
                if i-1>=0:
                    queue.append([i-1,j,3,count+1])
                if i+1<len(arr):
                    queue.append([i+1,j,4,count+1])
                j-=1
        if huong==2:
            while j<len(arr[0]) and arr[i][j]!='#' and arr[i][j]!='s':
                if arr[i][j]=='g':
                    return count
                if i-1>=0:
                    queue.append([i-1,j,3,count+1])
                if i+1<len(arr):
                    queue.append([i+1,j,4,count+1])
                j+=1
        if huong==3:
            while i>=0 and arr[i][j]!='#' and arr[i][j]!='s':
                if arr[i][j]=='g':
                    return count
                if j-1>=0:
                    queue.append([i,j-1,1,count+1])
                if j+1<len(arr[0]):
                    queue.append([i,j+1,2,count+1])
                i-=1
        if huong==4:
            while i<len(arr) and arr[i][j]!='#' and arr[i][j]!='s':
                if arr[i][j]=='g':
                    return count
                if j-1>=0:
                    queue.append([i,j-1,1,count+1])
                if j+1<len(arr[0]):
                    queue.append([i,j+1,2,count+1])
                i+=1
    return -1
def main(lines):
    arr=[]
    kichthuoc=lines[0].split(" ")
    for i in range(1,int(kichthuoc[0])+1):
        a=[j for j in lines[i]]
        arr.append(a)
    print(rook(arr))

if __name__ == '__main__':
    lines1 = ["9 9",
            "g..##...#",
            "........#",
            "....#....",
            "#....#.#.",
            ".#.......",
            ".....#...",
            ".....#...",
            ".........",
            "..#.#..#s"]
            
    lines2=["8 10",
            "g.......#.",
            ".....#.##.",
            "#.......#.",
            ".#..#.....",
            "......##..",
            ".....###..",
            ".#.....#..",
            "##.......s"]

    lines4=["9 8",
            "g.......",
            "........",
            "..##..#.",
            "..#...#.",
            ".......#",
            ".#..#...",
            "..#.###.",
            "..#.....",
            "....##.s"]
    main(lines4)