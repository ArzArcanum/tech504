# SET VARIABLE user_prompt TO TRUE
user_prompt = True

# PUT BEGINNING OF WHILE LOOP HERE - SHOULD LOOP WHILE user_prompt IS TRUE
while user_prompt:
    age = input("What is your age? ")
    # PUT IF STATEMENT HERE TO CHECK IF age IS ALL DIGITS
    if age.isdigit() and int(age) <= 117:
        # SET user_prompt TO FALSE
        user_prompt = False
    # ADD ELSE STATEMENT HERE
    else:
        # TELL USER THE PROBLEM WITH THEIR INPUT
        print("ERROR: your input must only contain digits, and must be equal or lower than 117")

print(f"Your age is {age}")
