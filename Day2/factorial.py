import time

start = time.time()


def factorial(n):
    if n < 1:
        return 1
    else:
        returnNumber = n * factorial(n - 1)  # recursive call
        print(str(n) + '! = ' + str(returnNumber))
        return returnNumber
    factorial()


def factorial_loop():
    n = int(input("Enter number:"))
    fact = 1
    while n > 0:
        fact = fact * n
        n = n - 1
    print(fact)
    end = time.time()
    a = end - start
    print("This operation took " + str(a) + " milliseconds.")
    b = input("Would you like to restart?")
    if b == 'Yes':
        factorial_loop()


def welcome():
    greeting = input("Welcome! Would you like to calculate a factorial using recursion or using a while loop?")
    if greeting == "Recursion":
        factorial(n)
		n = int(input("Input a number: "))
    if greeting == "While Loop":
        factorial_loop()
		n = int(input("Input a number: "))
    else:
        print("That value is invalid. Restarting now.")
        welcome()


welcome()


end = time.time()
a = end-start
print("This operation took " + str(a) + " milliseconds.")

