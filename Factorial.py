def Factorial(n):
    if n == 0:
        return 1

    if n > 0:
        return n * Factorial(n - 1)


def is_integer(n):
    try:
        float(n)
    except ValueError:
        return False
    else:
        return float(n).is_integer()


print('--------------------------------------------------------')
print("Hello!, this is a simple factorial calculation script")
print('To quit, press the "q" key')
print('--------------------------------------------------------')

while True:
    a = input("Enter a positive integer number to find its factorial: ")

    print('--------------------------------------------------------')

    if a == 'q':
        quit()

    try:
        if isinstance(float(a), float) == True and is_integer(a) == False:
            print("Can't find the factorial of a fractional number")
            print('--------------------------------------------------------')
        else:
            b = int(a)

            if b < 0:
                print("Can't find the factorial of a negative number")
                print('--------------------------------------------------------')
            else:
                print("The factorial is:", Factorial(b))
                print('--------------------------------------------------------')
    except ValueError:
        print('Invalid Input, Try again')
        print('--------------------------------------------------------')
