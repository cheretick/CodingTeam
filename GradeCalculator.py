project = eval(input("Project Grade: "))
homework = eval(input("Homework Grade: "))
quiz = eval(input("Quiz Grade: "))
attendance = eval(input("Attendance Grade: "))
exam = eval(input("Exam Grade: "))

finalPercent = (project * .4 + \
    homework * .05 + \
    quiz * .1 + \
    attendance * .05 + \
    exam * .4)

print("Final Grade: " + format(finalPercent, ".2f") + "%")
