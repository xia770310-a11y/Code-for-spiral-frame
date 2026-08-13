a, b=map(int, input().split())
matrix=[]
for i in range(a):
    matrix.append(list(map(int, input().split())))
for j in range(a):
    for k in range(b):
        c=1
        if matrix[j][k]==0:
            while j+c<a-1 and matrix[j+c][k]==0:
                c=c+1
            hormax=matrix[j+c][k]-c
            c=1
            while k+c<b-1 and matrix[j][k+c]==0:
                c=c+1
            vertmax=matrix[j][k+c]-c
            matrix[j][k]=min(hormax, vertmax)
print(sum(sum(row) for row in matrix))