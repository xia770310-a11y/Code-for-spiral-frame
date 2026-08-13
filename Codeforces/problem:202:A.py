text=input()
list=[ord(char) for char in text]
x, y=max(enumerate(list))
print(text[x]*(list.count(y)))