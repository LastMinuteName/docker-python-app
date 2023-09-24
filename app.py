def main():
    print("Number multiplying app")
    
    while True:
        while True:
            number1 = input("Input your first number: ")
            if (checkIfInt(number1)):
                break

        while True:
            number2 = input("Input your second number: ")
            if (checkIfInt(number2)):
                break
        
        result = int(number1)*int(number2)
        print(f"{number1} x {number2} = {result}")

def checkIfInt(input):
    try:
        val = int(input)
        return True
    except ValueError:
        return False

if __name__ == "__main__":
    main()