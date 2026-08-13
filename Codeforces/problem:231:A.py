x=0
n=int(input())
for i in range(n):
    num1, num2, num3=input().split()
    list=[num1, num2, num3]
    if list.count('1')>=2:
        x=x+1
print(x)