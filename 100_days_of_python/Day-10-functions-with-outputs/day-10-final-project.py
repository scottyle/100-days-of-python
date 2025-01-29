import art

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

#If we just call the function we can just store it rather than trigger it like this add(), subtract()
operations_dict = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
}

def calculator():
    print(art.logo)
    should_continue = False
    num1 = float(input("What is your first number?: "))

    while not should_continue:
        for key in operations_dict:
            print(key)

        operations = input("Pick an operation: ")
        num2 = float(input("What is your second number?: "))
        answer = operations_dict[operations](num1, num2)
        print(f'{num1} {operations} {num2} is {answer}')

        calculation_continue = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ")

        if calculation_continue == 'n':
            print("\n" * 100)
            should_continue = True
            calculator()
        elif calculation_continue == 'y':
            num1 = answer


calculator()





