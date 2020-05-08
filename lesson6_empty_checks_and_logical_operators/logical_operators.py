def main():
    students = ["Kidu", "Hareg"]

    name = input("What is your name? ")

    if name not in students:
        print("You are not a student")
    else:
        print("You are a student")

    # if name in students:
    #     print("You are a student")
    # else:
    #     print("You are not a student")

    # Second example
    value = False

    if not value:
        print("Value is false")
    else:
        print("Value is true")


if __name__ == '__main__':
    main()
