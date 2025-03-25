a = int(input("enter the first number: "))
b = int(input("enter the second number: "))
c= str(input("enter the operator: "))
if c == "+":
    print("the sum is: " ,a+b)
elif c=="-":
    print("the difference is: ",a-b)
elif c=="*":
    print("the product is: " , a*b)
elif c=="**":
    print("the power is: ", a**b)
elif c=="/":
    if b != 0:
        print("the division is: ", a/b)
    else :
        print("cann't divide by zero")
elif c=="//":
    if b != 0:
        print("the quotient is: ", a//b)
    else :
        print("cann't divide by zero")
elif c=="%":
    if b != 0:
        print("the remainder is: ", a%b)
    else:
        print("cann't divide by zero")
else :
    print("Invalid operator")
