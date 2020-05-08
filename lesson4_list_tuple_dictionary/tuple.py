# tuple is immutable - you cannot add or remove an element from a tuple
def main():
    tuple = (32, 29, 27)
    print(tuple)

    # accessing tuple using indexes
    print(tuple[0:-1]) # prints (32, 29) # last index in not included

    # you can convert a tuple to a list
    # like you covert an integer to a string or vice versa
    converted_list = list(tuple)
    print(converted_list)


if __name__ == '__main__':
    main()