print("Calculator")
print("Calculators")
print("1:ADD")
print("2:SUB")
print("3:MUL")
print("4:DIV")
x=int(input("Enter the operation you want do execute: "))
if x==1:
    a=int(input("Enter the 1st number: "))
    b=int(input("Enter the 2nd number: "))
    print("Addition of numbers is:",a+b)

if x==2:
    a=int(input("Enter the 1st number: "))
    b=int(input("Enter the 2nd number: "))
    print("Subtraction of number is:",a-b)

if x==3:
    a=int(input("Enter the 1st number: "))
    b=int(input("Enter the 2nd number: "))
    print("Multiplication number is:",a*b)

if x==4:
    a=int(input("Enter the 1st number: "))
    b=int(input("Enter the 2nd number: "))
    print("Division of number is:",a/b)

else:
    print("choos correct option")



