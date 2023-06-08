# functions
def ReadFromFileToDict (path):
    file = open(path, "r")

    inner_students_dict = {"Invalid Grades": []}

    for line in file:
        # variables declaration
        grades_list = []
        is_invalid = False

        # line parsing
        name_grades_list = line.split(':')
        name = name_grades_list[0].strip()
        pre_grades_list = name_grades_list[1].split(',')

        # line validation
        for pre_grade in pre_grades_list:
            pre_grade = pre_grade.strip()

            # 1) must be in range (0-100) and be a number
            try:
                grade = float(pre_grade)

                if not(0 <= grade <= 100):
                    is_invalid = True
                    break
                else:
                    grades_list.append(grade)
            except:
                is_invalid = True
                break

        # filling the dictionary according to validation results
        if is_invalid:
            inner_students_dict["Invalid Grades"].append(name)
        else:
            average_grade = sum(grades_list) / len(grades_list)

            if average_grade > 60:
                inner_students_dict[name] = average_grade
            else:
                inner_students_dict[name] = 'F'

    return inner_students_dict
    file.close()


def WriteFromDictToFile (dict, path):
    file = open(path, "w")
    for key in dict:
        if key == "Invalid Grades":
            for student in dict[key]:
                file.write("{}:\n".format(student))
            continue
        file.write("{}: {}\n".format(key, dict[key]))


# main part
STUDENTS_DICT = ReadFromFileToDict("M03L01_input.txt")
WriteFromDictToFile(STUDENTS_DICT, "M03L01_output.txt")
