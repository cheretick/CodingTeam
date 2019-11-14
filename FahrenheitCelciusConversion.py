number = eval(input("Enter a temperature: "))
unit = input("Enter F for Fahrenheit or C for Celcius: ")

if unit == 'F':
    conversion = (number - 32) * 5/9
    print(number, "F is", conversion, "C")

if unit == 'C':
    conversion = (number * 9/5) + 32
    print(number, "C is", conversion, "F")