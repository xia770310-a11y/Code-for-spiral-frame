t=int(input())
for i in range(t):
    k=int(input())
    brackets=list(input())
    balance=0
    minbalance=0
    for i in range(k):
        if brackets[i]=="(":
            balance=balance+1
        else:
            balance=balance-1
        minbalance=min(minbalance, balance)
    print(abs(minbalance))