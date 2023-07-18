
print("select an operation: ")

print("1. ADD")
print("2. SUBSTRACT")
print("3. MULTIPLY")
print("4. DIVIDE")
print("5. SQUARE")
print("6. PERCENTAGE")


operation =input()

if operation == "1":
    num1 =int(input("enter first number: "))
    num2 =int(input("enter second number: "))
    sum=num1+num2
    print("the sum is " ,sum)
elif operation == "2":
    num1 = int(input("enter first number: "))
    num2 = int(input("enter second number: "))
    sum=num1-num2
    print("the sum is " ,sum)
elif operation == "3":
    num1 = int(input("enter first number: "))
    num2 = int(input("enter second number: "))
    sum=num1*num2
    print("the sum is " ,sum)
elif operation == "4":
    num1 = int(input("enter first number: "))
    num2 = int(input("enter second number: "))
    sum=num1/num2
    print("the sum is " ,sum)
elif operation == "5":
    num = int(input("enter number: "))
    sum=num*num
    print("the sqare is " ,sum)
elif operation == "6":
    num1 = int(input("enter first number: "))
    num2 = int(input("enter second number: "))
    sum=num1/100*num2
    print("the sum is " ,sum)

else:
    print("invalid entry")
