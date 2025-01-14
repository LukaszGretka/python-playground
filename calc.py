def main():
    while True:
        print("______________________________")
        print("Select operation number (1-4):")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        try:
            operation: int = int(input("Enter operation number: "))
        except ValueError:
            print("Invalid operation number. Please try again.")
            continue

        if(operation < 1 or operation > 4):
            print("Invalid operation number. Please try again.")
            continue
        
        try:
            number1Input: str = input("Enter the first number: ")
            number2Input: str = input("Enter the second number: ")

            if len(number1Input) > 100:
                print("First number is too long. Please try again.")
                continue
            if len(number2Input) > 100:
                print("Second number is too long. Please try again.")
                continue
        except ValueError:
            print("Invalid input. Please try again.")
            continue
        
        number1 = float(number1Input)
        number2 = float(number2Input)

        result: float
        if operation == 1:
            result = sum(number1, number2)
        elif operation == 2:
            result = subtract(number1, number2)
        elif operation == 3:
            result = multiply(number1, number2)
        elif operation == 4:
            if(number2 == 0):
                print("Cannot divide by zero. Please try again.")
                continue
            result = divide(number1, number2)
        
        if result.is_integer():
            result = int(result)

        print("------------------------------")
        print("Result: ", result)
        print("------------------------------")
        input("Click any key to continue...")

def sum(number1: float, number2: float) -> float:
    return number1 + number2

def subtract(number1: float, number2: float) -> float:
    return number1 - number2

def multiply(number1: float, number2: float) -> float:
    return number1 * number2   

def divide(number1: float, number2: float) -> float:
    return number1 / number2

if __name__ == "__main__":
    main()