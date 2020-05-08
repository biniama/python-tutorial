# Functions
# Purpose
# 1. Structuring our code into multiple packages
# 2. Re-usability


def greeting(first_name, last_name):   # first_name is an argument
    print(f'Hello {first_name} {last_name}!')


def goodbye(first_name):
    print(f'Bye {first_name}!')


if __name__ == '__main__':
    greeting('Hareg', 'Berhanu')
    greeting('Kidu', 'Lakew')

    # Passing named arguments
    greeting(last_name='Biniam', first_name='Naod')

    # The following is an error
    # greeting(last_name='Biniam', 'Naod')
    greeting('Naod', last_name='Biniam')

    # calling functions with different arguments
    goodbye('Hareg')
    goodbye('Kidu')

    # names = ['Hareg', 'Kidu', 'Bini']
    # for name in names:
    #     greeting(name)
