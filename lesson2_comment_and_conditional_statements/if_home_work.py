# Home Work
# Write a program that informs the user if he is a coronavirus suspect.
# A user is a suspect if s/he is older than 65 and has been to China or Italy and
# has a previous respiratory disease.

# Description of data types
# name = 'Biniam'   # type - string
# age = 32          # type - int
# is_light_on = 1/0 # type - bool or boolean - value can be either true (1) or false (0)


def main():
    print('Welcome to COVID-19 Online Test')

    # Step 1: Accept input from the User
    age = int(input('Please enter your age '))

    travel_history = input('Where have you traveled recently? ')

    previous_disease = input('Do you have respiratory diseases? (yes/no) ')

    # Step 2: Check condition and print response
    # other option: travel_history.lower() in ('china', 'italy', 'usa')

    if age > 65 and \
            travel_history.upper() in ('CHINA', 'ITALY', 'USA') and \
            previous_disease.lower() == 'yes':
        print('You are a suspect. Please call 911')
    else:
        print('You are not a suspect')

    print('Take care and wash your hands! again!')


if __name__ == "__main__":
    main()
