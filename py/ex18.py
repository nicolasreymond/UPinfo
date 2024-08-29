# Define the factorial function
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Main program
def calculate_euler_approximation(n):
    e_approximation = 0
    for i in range(n + 1):
        e_approximation += 1 / factorial(i)
    return e_approximation

# Input the order n
n = int(input("Enter the order n to approximate e: "))

# Calculate and display the approximation of e
e_value = calculate_euler_approximation(n)
print(f"The approximation of e for order {n} is: {e_value}")
