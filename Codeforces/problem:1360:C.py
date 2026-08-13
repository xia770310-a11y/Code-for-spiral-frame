k=int(input())
for i in range(k):
    t=int(input())
    noob=True
    count=0
    c=0
    numbers=list(map(int, input().split()))
    for i in range(t):
        if numbers[i]% 2 == 0:
            count=count+1
    if count% 2 == 0:
        print("YES")
    else:   
        while noob==True and c<t-1:
            if sorted(numbers)[c+1]-sorted(numbers)[c]==1:
                print("YES")
                noob=False
            else:
                c=c+1
        if noob==True:
            print("NO")