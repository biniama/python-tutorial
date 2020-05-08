#  list is mutable - you can change the value.
def main():
    # age_biniam = 32
    # age_kidan = 29
    # age_hareg = 27
    # print(f'{age_biniam} {age_kidan} {age_hareg}')

    # defining list
    age_list = [32, 29, 27]

    # printing the whole list
    print(age_list)

    # adding an element to a list
    age_list.append(30)

    # printing the whole list
    print(age_list)

    # deleting an element from a list - deletes the last element
    age_list.pop()

    # printing the whole list
    print(age_list)

    # deleting a specific element from the list using the index
    age_list.pop(0)

    # printing the whole list
    print(age_list)

    # deleting a specific element from the list using the value
    age_list.remove(29)

    # printing the whole list
    print(age_list)

    # # iterating/looping over a list
    # for age in age_list:
    #     print(age)


if __name__ == '__main__':
    main()