# A Simple Calculator
a=float(input("Enter the first number:"))
b=float(input("Enter the second number:"))
print(" Choose an operation")
print(" 1.Addition")
print(" 2.subtraction")
print(" 3.multiplication")
print(" 4.division")
choice= input(( "enter any no (1-4):"))

if choice == "1":
    print("Result=",a+b)
elif choice=="2":
    print("Result=",a-b)
elif choice=="3":
    print("Result=",a*b)
elif choice=="4":
    if b==0:
        print("cannot be divisible by 0")
    else:
        print("Result=", a/b)
else:
        print("INVALID")