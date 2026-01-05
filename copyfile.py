with open("a.txt") as f:
    content=f.read()
with open("b.txt","w") as f:
    f.write(content)