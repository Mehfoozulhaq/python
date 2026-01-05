spam1= "click on the link"
spam2="subscribe"

x= input("Enter the message: ")

if(spam1 in x.lower() or spam2 in x.lower()):
    print("this message is spam")
else:
    print("this message is not a spam")