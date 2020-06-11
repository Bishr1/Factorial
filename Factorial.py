def Factorial(n):
    if n == 0:
        return 1

    if n > 0:
        return n * Factorial(n - 1)


print('')
print("Hello!, this is a simple Factorial calculation script")
print('To quit, hit the q key')
print('')

while True:
    a = input("Enter a positive integer to find its Factorial: ")

    print('')

    if a == 'q':
        quit()

    try:
        b = int(a)

        if b < 0:
            print("Can't find the Factorial of a negative number")
        else:
            print("The Factorial is:", Factorial(b))
            print('')
    except ValueError:
        print('Invalid Input, Try again')
        print('')
