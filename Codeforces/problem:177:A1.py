n=int(input()), array=[], uppdia=0, lowdia=0
for i in range(n):
    row=list(map(int, input().split()))
    array.append(row)
for i in range((n//2)):
    uppdia+=array[i][i]+array[i][n-i-1]
    lowdia+=array[n-i-1][i]+array[n-i-1][n-i-1]
print(uppdia+lowdia+sum(array[(n//2)])+sum(row[n//2] for row in array)-array[n//2][n//2])