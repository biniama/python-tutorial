def main():
    # call a function and accept the returned value
    # you can give any name to the returned value
    returned_all_employees = accept_employee_data()

    # pass the returned value from the previous function to the next function
    returned_all_employees_with_bonus = calculate_bonus(returned_all_employees)

    # pass the returned value from the previous function to the next function
    print_employee_data(returned_all_employees_with_bonus)


# define a function
def accept_employee_data():
    # Accept 3 employees data
    all_employees = []
    for i in range(3):
        name = input('Enter your name: ')
        date_of_birth = input('Enter your date of birth: ')
        year_of_experience = int(input('Enter year of experience: '))

        # Input Validation below - commented out
        # year_of_experience_input = input('Enter year of experience: ')
        # if not year_of_experience_input.isnumeric():
        #     print('Error. Please enter year of exp as number')
        #     return
        # year_of_experience = int(input('Enter year of experience: '))

        salary = int(input('Enter your salary: '))

        # Store employee data in dictionary
        employee_data = {
            'name': name,
            'date_of_birth': date_of_birth,
            'year_of_experience': year_of_experience,
            'salary': salary,
        }

        # Store all employees data in list
        all_employees.append(employee_data)
    # at the end, tell the caller what the list of all employees is
    return all_employees


# define a function with argument i.e. all_employees
def calculate_bonus(all_employees):
    all_employees_with_bonus = []

    # Calculate bonus
    for employee in all_employees:
        if employee.get('year_of_experience') >= 5:
            new_salary = employee.get('salary') * 0.05 + employee.get('salary')
            # add new_salary to the dictionary
            employee['new_salary'] = new_salary
        else:
            # if experience is less than 5 years, save the salary as new salary
            employee['new_salary'] = employee.get('salary')
        all_employees_with_bonus.append(employee)
    return all_employees_with_bonus


def print_employee_data(all_employees):
    # print the heading
    print(f'Name\tDate of birth\tExperience\tSalary\tNew Salary')

    # Print employee data
    for employee in all_employees:
        print(
            f"{employee.get('name')}\t{employee.get('date_of_birth')}\t\t\t{employee.get('year_of_experience')}\t\t{employee.get('salary')}\t\t{employee.get('new_salary')}")


if __name__ == '__main__':
    main()
