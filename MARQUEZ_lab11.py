student_list = []
passed_list = []
student_grade = input("Student grade: ")

while True:
    if student_grade.lower() == "done":
        break 
        
    elif student_grade.isdigit():
        student_grade = int(student_grade)
        if (student_grade < 40) or (student_grade > 100):
            print("Invalid!\nGrade must be between 40 and 100")
            student_grade = input("Student grade: ")
            continue

        else:
            if student_grade >= 75:
                passed_list.append(student_grade)
                student_list.append(student_grade)
                student_grade = input("Student grade: ")
                continue
            
            else: 
                student_list.append(student_grade)
                student_grade = input("Student grade: ")
                continue
            
    else:
        print("Invalid!\nMust enter valid grade")
        student_grade = input("Student grade: ")
        continue


average = sum(student_list) / len(student_list)
passed_ave = sum(passed_list) / len(student_list)
print(f"Class Average Grade: %{average:.2f}")
print("Students Passed:", len(passed_list))
print(f"Percentage of passed students: %{passed_ave:.2f}")
print(passed_list)

