# Function to add four numbers
def add_four_numbers(num1, num2, num3, num4):
    return num1 + num2 + num3 + num4

# Main function to get input from the user and display the result
def main():
    # Get input from the user
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    num3 = float(input("Enter the third number: "))
    num4 = float(input("Enter the fourth number: "))

    # Calculate the sum
    result = add_four_numbers(num1, num2, num3, num4)

    # Display the result
    print("The sum of the four numbers is:", result)

# Run the main function
if __name__ == "__main__":
    main()
