#Roy Jose T. Manangan
#8-Camia

def display_header():
    print("Student Performance Evaluator")

def get_student_info():
    global first_score, second_score, third_score, name
    name = input("What is your name?")
    first_score = int(input("What is your first assessment score?"))
    second_score = int(input("What is your second assessment score?"))
    third_score = int(input("What is your third assessment score?"))



def evaluate_performance():
    average = (first_score + second_score + third_score) / 3
    return average

def display_report():
    print(f"{name} got {first_score}, {second_score}, {third_score} and their average is {evaluate_performance()}")
    if evaluate_performance() <= 100:
        print("Outstanding!")
    elif evaluate_performance() <= 90:
        print("Very Satisfactory!")
    elif evaluate_performance() <= 85:
        print("Satisfactory.")
    elif evaluate_performance() <= 80:
        print("Fairly Satisfactory.")
    elif evaluate_performance() < 75:
        print("Needs Improvement.")
    else:
        print("Invalid Grade")

display_header()
get_student_info()
evaluate_performance()
display_report()