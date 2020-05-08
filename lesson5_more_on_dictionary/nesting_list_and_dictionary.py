def main():
    # It is possible to nest/add dictionaries in a list.
    # It is also possible to nest/add list in a dictionary

    persons = [
        {
            'name': 'Biniam',
            'age': 32,
            'spouse': 'Kidu',
            'kids': [
                'Hasset',
                'Naod'
            ]
        },
        {
            'name': 'Kidan',
            'age': 28
        },
        {
            'name': 'Hareg',
            'age': 23
        }
    ]

    print(persons)


if __name__ == "__main__":
    main()