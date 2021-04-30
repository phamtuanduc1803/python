array =[[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]]

cols, rows = len(array[0]), len(array)

border = set([(i, 0     ) for i in range(rows)] + 
             [(i, cols-1) for i in range(rows)] + 
             [(0, i     ) for i in range(cols)] + 
             [(rows-1, i) for i in range(cols)])
print(border)
lowest  = min(array[x][y] for (x, y) in border) 
highest = max(map(max, array))                 
import collections
fringes = collections.defaultdict(set)
for (x, y) in border:
    fringes[array[x][y]].add((x, y))

fill_height = [[None for _ in range(cols)] for _ in range(rows)]

for height in range(lowest, highest + 1):
    while fringes[height]:
        (x, y) = fringes[height].pop()
        fill_height[x][y] = height
        for x2, y2 in [(x-1, y), (x, y-1), (x+1, y), (x, y+1)]:
            if 0 <= x2 < rows and 0 <= y2 < cols and fill_height[x2][y2] is None:
                fringes[max(height, array[x2][y2])].add((x2, y2))
volume = sum(fill_height[x][y] - array[x][y] for x in range(rows) for y in range(cols))
print(volume)