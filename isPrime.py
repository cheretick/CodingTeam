def isPrime(n):
    for i in range(2, int(n**.5)):
        if n % i == 0:
            return False
        else:
            return True

num = eval(input("Enter a number: "))
if isPrime(num):
    print("The number is prime")
else:
    print("The number is not prime")