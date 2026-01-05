def greatest():
    a = int(input("enter ist no: "))
    b = int(input("enter 2nd no: "))
    c = int(input("enter 3rd no: "))
    if(a>b and a>c):
        print(f"{a} is the greatest")
    elif(b>c and b>a):
        print(f"{b} is the greatest")
    elif(c>a and c>b):
        print(f"{c} is the greatest")
    else:
        print("more than one numbers are greatest")

greatest()