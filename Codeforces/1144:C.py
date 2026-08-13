from collections import Counter
t=int(input())
my_list=list(map(int, input().split()))
if max(Counter(my_list).values())>2:
    print("NO")
else:
    print("YES")
    print(len(set(my_list)))
    print(sorted(set(my_list)))
    print(len(my_list)-len(set(my_list)))
    print(sorted(list(set([x for x in my_list if my_list.count(x) > 1])), reverse=True))