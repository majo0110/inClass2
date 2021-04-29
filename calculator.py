def main():
    #userChoice = input("Enter a number for calculator function: ")

    #userNum1 = input("Enter your first number: ")
    #userNum2 = input("Enter your first number: ")

    userNum1 = 10
    userNum2 = 2

    print( addition(userNum1,userNum2) )
    print( subtraction(userNum1,userNum2) )
    print( multiplication(userNum1,userNum2) )
    print( division(userNum1,userNum2) )


def addition(a,b):
    return (a+b)

def subtraction(a,b):
    return (a-b)

def multiplication(a,b):
    return (a*b)

def division(a, b):
    return (a/b)

if __name__ == '__main__':
    main()
