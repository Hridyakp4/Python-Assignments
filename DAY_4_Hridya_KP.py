def factorial(num):
    fact = 1
    if num == 0:
        return 1
    else:
        while(num>0):
            fact = fact*num
            num -= 1
        return fact

number = int(input("Enter number: "))
print(factorial(number))