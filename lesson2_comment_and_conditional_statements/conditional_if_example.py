def main():
    # Conditional Statements( if)
    # Example:
    # if kidu picks up her phone, then talk to her
    # otherwise( else ) send her text message

    # Can be written in Python as:
    # if username is ‘kiduhareg’ and password is 123456, then go to home screen.
    # else show error message

    # Conditional statement example
    # Assumption
    # child is someone who is less than 10 years old
    # young is someone who is between 10 - 30 years old
    # adult is someone who is between 30 - 50 years old

    # accepting input from the user
    ageString = input('Please enter your age ')
    age = int(ageString) # converts string to integer

    if age < 10:
        print('child')
    elif age >= 10 and age < 30:  # T and F = F, T and T = T
        print('young')
    elif age > 30 and age <= 50:
        print('adult')
    else:
        print('old - sheba')

    # another example with ‘if’ only
    # TODO: Un comment it to execute
    # if age < 10:
    #     print('child')
    # if age >= 10 and age <= 30:  # T and F = F, T and T = T
    #     print('young')
    # if age > 30:
    #     print('adult')


if __name__ == "__main__":
    main()

