def main():
    returned_persons = prepare_data()
    print_employee_data(returned_persons)


def prepare_data():
    persons = [
        {
            'name': 'Biniam',
            'age': 32
        },
        {
            'name': 'Kidan',
            'age': 28
        },
        {
            'name': 'Hareg',
            'age': 23
        }
    ]
    return persons


def print_employee_data(persons):
    print(f'Name\tAge')

    for person in persons:
        print(f"{person.get('name')}\t{person.get('age')}")


if __name__ == '__main__':
    main()
