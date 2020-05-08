def main():
    # Loop
    # find the sum of numbers from 1 to 10
    sum = 0
    for i in range(1, 11):  # the last value is non-inclusive
        sum = sum + i
    print('The sum of numbers from 1 to 10 is ' + str(sum))


if __name__ == "__main__":
    main()

