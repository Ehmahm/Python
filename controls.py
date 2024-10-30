# Program to return the grade of a student. Above 80 is A, 70 to 80 is B, then C, D, E, F

def grade(score):
    if score > 80:
        return 'A'
    elif score > 70:
        return 'B'
    elif score > 60:
        return 'C'
    elif score > 50:
        return 'D'
    elif score > 40:
        return 'E'
    else:
        return 'F'
    
print(grade(90))