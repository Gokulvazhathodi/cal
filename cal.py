
def add(x,y):
    return(x+y)

def subtract(x,y):
    return(x-y)

def multiply(x,y):
    return(x*y)

def divide(x,y):
    return(x/y)

def square(x):
    return(x*x)

print("select the option ")
print("1. addition")
print("2. substraction")
print("3. multiplication")
print("4. division")
print("5. square")



while(True):
    choice=int(input("enter the choice from (1/2/3/4/5)-->"))
    if choice in (1,2,3,4,5):
        if choice == 1:
            no1 = int(input("enter the first number->"))
            no2 = int(input("enter the second number->"))
            print("addition of two number",no1,"and",no2, "is->",add(no1,no2))
        elif choice == 2:
            no1 = int(input("enter the first number->"))
            no2 = int(input("enter the second number->"))
            print("subtraction of two number", no1, "and", no2, "is->", subtract(no1, no2))
        elif choice == 3:
            no1 = int(input("enter the first number->"))
            no2 = int(input("enter the second number->"))
            print("multiplication of two number", no1, "and", no2, "is->", multiply(no1, no2))
        elif choice == 4:
            no1 = int(input("enter the first number->"))
            no2 = int(input("enter the second number->"))
            print("division of two number", no1, "and", no2, "is->", divide(no1, no2))
        elif choice == 5:
            no1 = int(input("enter the first number->"))
            print("square of number", no1, "is->", square(no1))

        else:
            print("invalid ")
