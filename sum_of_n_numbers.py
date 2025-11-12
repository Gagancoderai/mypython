#Write a function sum_of_n_numbers() that accepts n numbers (entered by the user in a list) and returns their total sum
def sum_of_n_numbers(numbers_list):
    """Accepts a list of numbers and returns their total sum."""
    return sum(numbers_list)
user_input = input("Enter numbers separated by spaces: ")
try:
    numbers = [float(num) for num in user_input.split()]
    total_sum = sum_of_n_numbers(numbers)
    print(f"The sum of the entered numbers is: {total_sum}")
except ValueError:
    print("Invalid input. Please enter numbers separated by spaces.")
 Out put
 Enter numbers separated by spaces: 2
The sum of the entered numbers is: 2.0

