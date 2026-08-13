for i in range(int(input())):
    list1=list(map(int, input()))
    list2=list(map(int, input()))
    if sum(list1)!=sum(list2):
        print(-1)
    else:
        while list1!=list2 and len(list1)>1 and len(list2)>1:
            loopcount=1
            c=1
            while len(list1)-c>0 and list1[len(list1)-c]!=list2[len(list1)-c]:
                if list1[len(list1)-c-1]==sum(list1[len(list1)-1]+list1[len(list1)-i-1] for i in range(1, c))%10:
                    c=c+1
            k=1
            while len(list2)-c>0 and list1[len(list1)-c]!=list2[len(list1)-c]:
                if list2[len(list2)-k-1]==sum(list2[len(list2)-1]+list2[len(list2)-i-1] for i in range(1, k))%10:
                    k=k+1
            if c==k==1:
                print(loopcount)
                list1=[]
            if c>k:
                for i in range(k-1):
                    list2.pop()
                list2[len(list2)-2]=sum(list2[len(list2)-1]+list2[len(list2)-i-1] for i in range(1, k))%10
            else:
                for i in range(c-1):
                    list1.pop()
                list1[len(list1)-2]=sum(list1[len(list1)-1]+list1[len(list1)-i-1] for i in range(1, c))%10
            loopcount=loopcount+1
        else:
            print(1)
        
        