student_score = {
    "Harry" : 81,
    "Ron" : 78,
    "Hermione" : 99,
    "Draco" : 74,
    "Neville" : 62
}

student_grades = {}

def grade(score):
    if score >= 91:
        grade = "Outstanding"
    elif score >= 81:
        grade = "Exceeds Exprectations"
    elif score >= 71:
        grade = "Acceptable"
    else:
        grade = "Fail"
    
    return grade

for key in student_score:
    student_grades[key] = grade(student_score[key])

print(student_grades)