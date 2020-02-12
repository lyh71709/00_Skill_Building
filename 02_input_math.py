# get input

# ask user for name
username = input("What is your name? ")

# ask user for two numbers
integer_1 = int(input("What is your favourite number? "))
integer_2 = int(input("What is your second favourite number? "))

# add numbers together
addition = integer_1 + integer_2

# multiply numbers together
multiply = integer_1 * integer_2

# greet user and display math
print()
print("Hello", username)
print("{} + {} = {}".format(integer_1, integer_2, addition))
print("{} x {} = {}".format(integer_1, integer_2, multiply))