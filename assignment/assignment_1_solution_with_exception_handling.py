def main():
    # call a function and accept the returned value
    # you can give any name to the returned value
    returned_all_employees = accept_employee_data()

    # pass the returned value from the previous function to the next function
    returned_all_employees_with_bonus = calculate_bonus(returned_all_employees)

    # pass the returned value from the previous function to the next function
    print_employee_data(returned_all_employees_with_bonus)


def accept_employee_name():
    name = input('Enter your name: ')
    # as long as name is null, ask again! until the person አዛ እስኪሆን ድረስ!
    while not name:
        print('Name is required.')
        # the function calls itself
        name = accept_employee_name()
    return name


def accept_employee_date_of_birth():
    date_of_birth = input('Enter your date of birth: ')
    # as long as date_of_birth is null, ask again! until the person አዛ እስኪሆን ድረስ!
    while not date_of_birth:
        print('Date of Birth is required.')
        # the function calls itself
        date_of_birth = accept_employee_date_of_birth()
    return date_of_birth


def accept_employee_year_of_experience():
    # let's accept the year_of_experience as string before we convert it to integer
    year_of_experience_string = input('Enter year of experience: ')

    # as long as year_of_experience is null, ask again! until the person አዛ እስኪሆን ድረስ!
    while not year_of_experience_string:
        print('Year of Experience is required')
        # the function calls itself
        year_of_experience_string = accept_employee_year_of_experience()

    # now that we make sure that year_of_experience_string is not empty/not null
    # convert to integer
    try:
        year_of_experience = int(year_of_experience_string)
    except ValueError:
        print('Error occurred. The year of experience you entered is not a number.')
    else:
        return year_of_experience


def accept_employee_salary():
    # let's accept the salary as string before we convert it to integer
    salary_string = input('Enter your salary: ')

    # as long as salary is null, ask again! until the person አዛ እስኪሆን ድረስ!
    while not salary_string:
        print('Salary is required')
        # the function calls itself
        salary_string = accept_employee_salary()

    # now that we make sure that salary_string is not empty/not null
    # convert to integer
    try:
        salary = int(salary_string)
    except ValueError:
        print('Error occurred. The salary you entered is not a number.')
    else:
        return salary
    # finally:
    #     'Salary input accepted.'


# define a function
def accept_employee_data():
    # Accept 3 employees data
    all_employees = []
    for i in range(1):
        name = accept_employee_name()
        date_of_birth = accept_employee_date_of_birth()
        year_of_experience = accept_employee_year_of_experience()
        salary = accept_employee_salary()

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

    if not all_employees:
        print("Employee list is empty. I can't calculate bonus")
        return
        # This leaves this function but with no value.
        # It will stop processing the next lines
        # ታክሲ በባዶ እንደሚመለሰው

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

    if not all_employees:
        print("Employee list is empty. I can't print anything.")
        return
        # This leaves this function but with no value.
        # It will stop processing the next lines
        # ታክሲ በባዶ እንደሚመለሰው

    # print the heading
    print(f'Name\tDate of birth\tExperience\tSalary\tNew Salary')

    # Print employee data
    for employee in all_employees:
        print(
            f"{employee.get('name')}\t{employee.get('date_of_birth')}\t\t\t{employee.get('year_of_experience')}\t\t{employee.get('salary')}\t\t{employee.get('new_salary')}")


if __name__ == '__main__':
    main()
