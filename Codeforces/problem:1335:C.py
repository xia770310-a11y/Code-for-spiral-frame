k=int(input())
for i in range(k):
    k=input()
    noob=1
    skills=list(input().split())
    a=len(set(skills))
    b=len(skills)-a
    if a==len(skills)and a>1:
        print(1)
        noob=0
    if a==len(skills)and a==1:
        print(0)
        noob=0
    if noob==1:
        print(min(a,b))