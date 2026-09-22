#ROY JOSE T. MANANGAN,  TENY FAYE M. OBCENA, JAELLE ELYSE N. PALAGANAS
#8-CAMIA
#09/22/2026

# STUDENT AGE VALIDATOR

#Validation

valid_age = (12, 13, 14, 15, 16, 17, 18)

#Input
try:
    age = int(input("What is your age? "))
    if age in valid_age:
        print("Valid age")
    else :
            print("Invalid age")
except ValueError:
 print("Invalid input. Please enter a whole number.")