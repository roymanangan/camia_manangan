# ------------------------------------------------------------------------------------------------
# Jaelle Elyse Palaganas, Teny Faye Obcena, Roy Jose Manangan
# 8-Camia
# Username Validator
# ------------------------------------------------------------------------------------------------

# Ask for username

username = input("Enter username: ")

# .isalnum means alphabetical or numerical so we use it to verify if the username only has alnum values

# We also check if the length of the username is in between 5 and 10 characters with len()

if username.isalnum() and 5 <= len(username) <= 10:

    print("Valid username.")

# If these conditions aren't satisfied, the username is invalid

else:

    print("Invalid username.")

# ------------------------------------------------------------------------------------------------