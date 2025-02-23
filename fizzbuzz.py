def main():
    while True:
        try:
            n = int(input("Enter a number: "))
        except:
            print("Invalid input")
            continue
        
        for i in range(n):
            i = i + 1
            if i % 3 and i % 5 == 0:
                print('FizzBuzz', end= ' ')
            elif i % 3 == 0:
                print('Fizz', end= ' ')
            elif i % 5 == 0:
                print('Buzz', end= ' ')
            else:
                print(i, end= ' ')

        try:
            inpt = input("\nType 'exit' to close the program:\n")
        except:
            print("Invalid input")
            continue

        if inpt == "exit":
            break

if __name__ == "__main__":
    main()

