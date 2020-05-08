# User enters number 1234...
# Print One Two Three Four...


def main():
    number = input('Phone number: ')    # type => string
    # input() always returns string

    # validation
    if not number:  # the same as if number == ''
        print('You haven\'t entered a number. Bye.')
        # \ is called escape the next character and
        # it tells the compiler to escape or forget the next character

    number_mapping = {
        '1': 'One',
        '2': 'Two',
        '3': 'Three',
        '4': 'Four',
        '5': 'Five',
        '6': 'Six'
    }

    output = ''
    # loops over the individual numbers in the 'number' variable
    for character in number:
        # output = output + number_mapping.get(character, '?') + ' '
        output += number_mapping.get(character, '?') + ' '

        # x = x + 1 is the same as x += 1
        # x = x - 1 is the same as x -= 1
    print(output)

    # print(number_mapping[1])
    # print(number_mapping.get(2))
    # print(number_mapping['One']) # this will result in an error
    # print(number_mapping.get('One')) # prints None
    # print(number_mapping.get('One', 'One is not in the list')) # this provides detail/explanation


if __name__ == '__main__':
    main()