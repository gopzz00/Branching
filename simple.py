# A Simple Program: Greeting and Age Checker

# 1. Variables
name = input("Enter your name: ")  # Take user input for name
age = int(input("Enter your age: "))  # Take user input for age and convert it to an integer

# 2. Function to greet the user
def greet_user(name, age):
    """Function that greets the user and checks if they are an adult or minor."""
    print(f"Hello, {name}!")
    if age >= 18:
        print("You are an adult.")
    else:
        print("You are a minor.")

# 3. Calling the function
greet_user(name, age)
