# Function to calculate the year when the user will turn 100
def calculate_hundred_year(year_of_birth):
    return year_of_birth + 100

# Main function
def main():
    # Get user input
    name = input("What is your name? ")
    age = int(input("How old are you? "))

    # Calculate the year of birth
    current_year = 2024  # You can use datetime module to get the current year dynamically
    year_of_birth = current_year - age

    # Calculate the year they will turn 100
    year_turn_100 = calculate_hundred_year(year_of_birth)

    # Output the result
    print(f"Hello, {name}! You were born in {year_of_birth}.")
    print(f"You will turn 100 years old in the year {year_turn_100}.")

# Check if this is the main module and run the main function
if __name__ == "__main__":
    main()