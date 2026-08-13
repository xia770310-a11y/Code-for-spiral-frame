from collections import Counter
n, m=map(int, input().split())
array=[]
for i in range(n):
    row=list(input())
    array.append(row)
coordinates=[
    (r, c)
    for r, row in enumerate(array)
    for c, value in enumerate(row)
    if value=="*"]
xcoords, ycoords=zip(*coordinates)
print(min(Counter(xcoords), key=Counter(xcoords).get)+1, min(Counter(ycoords), key=Counter(ycoords).get)+1)