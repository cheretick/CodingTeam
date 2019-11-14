quit = False
grades = []
final = []
while not quit:
    userInput = input().lower().split()

    if userInput[0] == "add" or userInput[0] == "a":
        final.append(float(userInput[1]) * (float(userInput[2])/100))
        grades.append([float(userInput[1]),float(userInput[2])])

    if userInput[0] == "delete" or userInput[0] == "d":
        if len(grades) != 0:
            grades.pop()
            final.pop()

    if userInput[0] == "show" or userInput[0] == "s":
        if grades == []:
            print("Gradebook is empty")
        else:
            for i in range(len(grades)):
                print(grades[i][0], grades[i][1])
            print("Total Grade: " + format(sum(final), ".2f") + "%")

    if userInput[0] == "clear" or userInput[0] == "c":
        grades = []
        final = []

    if userInput[0] == "help" or userInput[0] == "h":
        print(format("HELP", "^80") + "\n" + "-" * 80 + \
              "\n\tEnter the following commands, followed by indicated values."
              "\n\tSeparate values with spaces (not case sensitive)\n\n"
              "Command:\t\tDetails:\n"
              "\"add\" or \"a\"\t\tAdds a new grade to the grade book with custom weight.\n\t\t\t\t\t"
              "EX: \"add 95 15\" adds a grade of 95%, weighted at 15% "
              "\n\n\"delete\" or \"d\"\t\tRemoves the last grade entered from the grade book"
              "\n\n\"show\" or \"s\"\t\tDisplays the grade book's entries as well as the total grade percentage"
              "\n\n\"clear\" or \"c\"\t\tClears the grade book"
              "\n\n\"quit\" or \"q\"\t\tQuits the program")

    if userInput[0] == "quit" or userInput[0] == "q":
        quit = True