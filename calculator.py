class calculator:
    def __init__(self):
        pass

    def add(self, num1, num2):
        return num1 + num2

    def substract(self, num1, num2):
        return num1 - num2

    def multiplication(self, num1, num2):
        return num1 * num2

    def devided(self, num1, num2):
        return num1 / num2 

    def power(self, num1, num2):
        return num1 ** num2

calc = calculator()

num1 = float(input('enter a valu'))
num2 = float(input('enter a valu'))
operator = input('Enter operator (+, -, *, /): ')

if operator == '+':
    result = calc.add(num1, num2)
elif operator == '-':
    result = calc.substract(num1, num2)
elif operator == '*':
    result = calc.multiplication(num1, num2)
elif operator == '/':
    result = calc.devided(num1, num2)
elif operator == '**':
   result = calc.power(num1, num2)
else:
    print('enter a valid operatior')

print(result)

