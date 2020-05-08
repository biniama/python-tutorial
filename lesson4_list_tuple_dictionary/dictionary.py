def main():
    # dictionary has a key and a value and use colon (:) in between
    # this is a very powerful and useful data type
    dictionary = {"Book": "is something to read"}
    print(dictionary)

    biniam_data = {
        "name": "Biniam",
        "age": 32,
        "profession": "Senior Software Engineer",
        "spouse": {
            "name": "Kidan",
            "age": 29
        }
    }
    print(biniam_data)

    hareg_data = {
        "name": "Hareg",
        "age": "26",
        "profession": "Junior Programmer and Business Manager"
    }
    print(hareg_data)

    # Using for loop to iterate/repeat over a dictionary
    # Exercise: print Hareg's data in capital letter and as a statement

    for key in hareg_data:
        #print(key.upper() + ' IS ' + hareg_data.get(key).upper())
        # alternative way of writing
        print(f'{key.upper()} IS {hareg_data.get(key).upper()}')


if __name__ == '__main__':
    main()
