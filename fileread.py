'''f=open("file.txt")
data=f.read()
print(data)
f.close()'''
#with statement -> we don't have to close the file
with open("file.txt") as f:
    data=f.read()
print(data)