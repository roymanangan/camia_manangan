#Roy Jose T. Manangan
#8-Camia
#Sum and Difference Calculator

#Global
input1 = int(input("What is the first number?"))
input2 = int(input("What is the second number?"))

def calculate_sum():
    global input1, input2
    #local
    sum = input1 + input2
    print("The sum is", sum)
    return sum

def calculate_difference():
    global input1, input2
    #local
    difference = input1 - input2
    print("The difference is", difference)
    return difference

calculate_sum()
calculate_difference()