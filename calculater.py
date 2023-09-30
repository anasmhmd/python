a=int(input("Enter a number"))
b=int(input("enter the second number"))
c=input("+\n-\n*\n/\n%\n enter the operation")
if c=="+":
    print(a+b)
elif c=="-":
    print(a-b)
elif c=="*":
    print(a*b)
elif c=="/":
    print(a/b)
elif c=="%":
    print(a%b)
else:
    print("Wrong input")
