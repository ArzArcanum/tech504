# •	Comments in the code are to help you meet user requirements, but you may need to write code in the order you think is necessary
# User story 1
# As a user, I want to be able to guess a number and know if i got it correct or not, so that I can know if I won or not.

# Define/assign number to a variable called magic_number
magic_number = 42
number_of_guesses = 5
# Ask user for input
valid_input = False
# def take_input():

for guess in range(number_of_guesses):
    while not valid_input:
        try:
            current_guess = int(input("What is your guess?"))
            valid_input = True
        except:
            print("Invalid input. Please try again.")

    if current_guess == magic_number:
        print("You guessed right!")
        break
    else:
        valid_input = False
        if current_guess < magic_number:
            print("You guessed too low!")
        else:
            print("You guessed too high!")

# Check if this input matches magic_number


# Let the user know if the response was correct or not


# Allow the user 5 guesses

