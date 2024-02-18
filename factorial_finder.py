def factorial(num):
    if num == 1:
        return 1
    else:
        return num * factorial(num-1)
    
value = int(input('enter a number: '))
result = factorial(value)
print(f'The factorial of {value} is {result}')

#lets check if it worked