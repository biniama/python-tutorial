def main():

    # Print 'F'
    #   *****
    #   **
    #   *****
    #   **
    #   **
    numbers = [5, 2, 5, 2, 2]

    for r in numbers:
        for c in range(0, r):
            print('*', end='')  # Print with out new line
        print('')

    # HOW THE COMPUTER WORKS
    # MEMORY
    # numbers = [5, 2, 5, 2, 2]
    # r = 5
    # c = 0
    #
    #
    # OUTPUT
    # *****
    # **
    # *****
    # **
    # **

    print('-------DIVIDER--------')

    # Print the following stars
    # *****
    # *****
    # *****
    # *****
    # *****
    for r in range(0, 5):
        for c in range(0, 5):
            print('*', end='')
        print('')


if __name__ == '__main__':
    main()