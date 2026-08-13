n=int(input())
scores=list(map(int, input().split()))
i=0
for k in range(n):
    while sum(scores)<4.5*n and scores[k]!=5:
        scores[k]=5
        i=i+1
print(i)