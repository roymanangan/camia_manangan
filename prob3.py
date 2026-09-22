#=====================================================================
#Teny Faye M. Obcena, Jaelle Elyse N. Palaganas, Roy Jose Manangan
#8 - Camia
#School Grade Validator
#=====================================================================

try:
    # Enter Valid Grade Levels
    valid_grade_levels = [7, 8, 9, 10, 11, 12]
    # Ask for User Input
    grade_level = int(input("Enter your grade level: "))

    # Validation
    if grade_level in valid_grade_levels:
        print("Valid grade level.")

    else:
        print("Invalid grade level.")

except ValueError:
    print("Invalid input. Please enter a whole number.")



