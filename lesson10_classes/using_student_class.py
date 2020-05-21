# from ethiopia.mymother import derkosh
# format for importing
# from foldername.filename import classname

from lesson10_classes.student import Student


def main():
    # define an object called hareg which is an instance/example/object of Student class
    hareg = Student(1, 'Hareg', 'Berhanu', 'IT', 98)

    # you can define as many objects as you want using the same class/blueprint
    kidu = Student(2, 'Kidu', 'Lakew', 'SE', 98)
    biniam = Student(3, 'Bini', 'Asnake', 'IS', 89)

    # calling the properties
    print(hareg.id)
    print(hareg.first_name)
    print(hareg.last_name)

    # calling the function - note the '()' at the end because we are calling a function
    print(hareg.full_name())

    print(kidu.full_name())

    print(biniam.full_name())


if __name__ == '__main__':
    main()
