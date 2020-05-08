# Home Work
def main():
    # PRINT THE FOLLOWING
    # *
    # **
    # ***
    # ****
    # *****
    # ******
    for r in range(0, 5):
        for c in range(0, r+1):
            print('*', end='')
        print('')

    print('-------DIVIDER--------')
    # PRINT THE FOLLOWING
    # 1 2 3 4 5
    # 1 2 3 4
    # 1 2 3
    # 1 2
    # 1
    for r in range(0, 5):
        for c in range(0, 5 - r):
            print(c + 1, end=' ')
        print('')

    print('-------DIVIDER--------')
    # PRINT THE FOLLOWING - BONUS
    # 5 4 3 2 1
    # 5 4 3 2
    # 5 4 3
    # 5 4
    # 5
    for r in range(0, 5):
        for c in range(5, r, -1):
            print(c, end=' ')
        print('')


if __name__ == '__main__':
    main()
