def main():
    all_students = accept_students_data()
    all_students_with_grade = calculate_grade(all_students)
    print_list_of_students(all_students_with_grade)


def accept_students_data():
    all_students = []
    number = int(input('Enter number of students: '))
    for i in range(number):
        name = input(f'Enter student {i + 1} name: ')
        id_number = int(input(f'Enter student {i + 1} id number: '))
        department = input(f'Enter student {i + 1} department: ')
        exam_result = int(input(f'Enter student {i + 1} exam result: '))
        students_data = {
            'name': name,
            'id': id_number,
            'department': department,
            'exam_result': exam_result,
        }
        all_students.append(students_data)
    return all_students


def calculate_grade(all_students):
    all_students_with_grade = all_students
    for student in all_students_with_grade:
        if student.get('exam_result') > 100 or student.get('exam_result') < 0:
            print(f"Error: Invalid grade {student.get('exam_result')}")
            student['grade'] = 'INVALID'
        elif student.get('exam_result') > 85:
            student['grade'] = 'A'
        elif student.get('exam_result') > 70:
            student['grade'] = 'B'
        elif student.get('exam_result') > 50:
            student['grade'] = 'C'
        elif student.get('exam_result') > 40:
            student['grade'] = 'D'
        else:
            student['grade'] = 'F'
    return all_students_with_grade


def print_list_of_students(all_students_with_grade):
    print("LIST OF STUDENTS TAKING 'Python Programming' CLASS")
    print('STUDENT ID\tSTUDENT NAME\tDEPARTMENT\tRESULT\tGRADE\t')
    for student in all_students_with_grade:
        print(f"{student.get('id')}\t\t\t\t{student.get('name')}\t\t\t"
              f"{student.get('department')}\t\t{student.get('exam_result')}"
              f"\t\t{student.get('grade')}")


if __name__ == '__main__':
    main()
