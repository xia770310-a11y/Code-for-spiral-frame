n, m=map(int, input().split())
scores=list(map(int, input().split()))
i=0
count=0
while sum(scores)>0 and scores[count]>=scores[m-1]:
    if scores[count]>scores[m-1]:
        count=count+1
        i=i+1
    if scores[count]==scores[m-1]:
        count=count+1
print(count)