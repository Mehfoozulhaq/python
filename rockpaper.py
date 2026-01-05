you= input("enter 'r' for rock 'p' for paper 's' for siccor: ")

di ={"r":1,"p":2 ,"s":3}
younum= di[you]
import random
computer= random.choice([1,2,3])
revdi={1:"rock",2:"paper",3:"siccor"}
comp=revdi[computer]
your=revdi[younum]
print(f"computer choosed {comp}")
print(f"you choosed {your}")

if(computer==younum):
    print("it is a draw!")
else:
    if(computer==1 and younum==2):
        print("you won!")
    elif(computer==1 and younum==3):
        print("You Lost!")
    elif(computer==2 and younum==1):
        print("you lost!")
    elif(computer==2 and younum==3):
        print("you won!")
    elif(computer==3 and younum==1):
        print("you won!")
    elif(computer==3 and younum==2):
        print("you lost!")
    else:
        print("something went wrong!")
