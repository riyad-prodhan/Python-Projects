

def calculator():

        num1 = float(input('enter a valu of num1'))
        num2 = float(input('enter a valu of num2'))
        operator = input('enter a operator like (+,-,*,/)')

        if operator == '+':
            result = num1 + num2
            print(result)
        elif operator == '-':
            result = num1 - num2
            print(result)
        elif operator == '*':
            result = num1 * num2
            print(result)
        elif operator == '/' and num2 != 0:
            result = num1 / num2
            print(result)
            
        else:
            print('enter the correct operator')

while True:
     calculator()