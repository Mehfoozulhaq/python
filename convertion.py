a= float(input("enter 1 to convert celcius to farenheit or 2 for farenheit to celcius: "))
if a==1:
   f=9/5*a+32
   print(f," deg farenheit")
elif a==2:
  c=(a-32)*5/9
  print(c,"deg celcius")
else :
   print("you entered wrong option")