# Exercise: write a program that checks username and password
# if username is ‘kiduhareg’ and password is 123456, then print go to home screen.
# if username is 'biniam' and password is 777, then
# print Hello Biniam, go to admin screen (on separate lines)
# else print error

# Variable Assignment in Python works just like Math except the position is reversed.
# g(x) = x + 1
# f(x) = x + 3
# x = 1
# f(g(x)) -> f(2) -> 5


def main():
    username = input('Please enter your username ')
    password = int(input('Please enter your password \n'))
    # \n means add a new line

    # = is used for assignment e.g. age = 32, name = 'Biniam'
    # == is used for comparison
    if username == 'kiduhareg' and password == 123456:
        print("""Hello,
Go to home screen.""")  # multi line comment
    elif username == "biniam" and password == 777:
        print("Hello, Go to admin screen")
    else:
        print('Sorry, error')


if __name__ == "__main__":
    main()
