# Function to add two numbers
def add_numbers(num1, num2):
    return num1 + num2

# Main function
def main():
    # Get user input
    try:
        number1 = float(input("Enter the first number: "))
        number2 = float(input("Enter the second number: "))
    except ValueError:
        print("Please enter valid numbers.")
        return

    # Calculate the sum
    result = add_numbers(number1, number2)

    # Display the result
    print(f"The sum of {number1} and {number2} is {result}.")

# Check if this is the main module and run the main function
if __name__ == "__main__":
    main()