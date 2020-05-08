# Importing and calling a function from another file
from .functions import greeting


def main():
    greeting('Naod', 'Biniam')


if __name__ == "__main__":
    main()
