# Example 1: Simple try-except
try:
    result = 1 / 0  # undefined -> ZeroDivisionError
    print(result)
except ZeroDivisionError:
    print("Dumb! You can't divide a number by zero. Go to first grade")

# Example 2: Advanced try-except-else-finally
try:  # try to do something
    age = int(input('Enter your age: '))  # can cause ValueError
    print(age)
except ValueError:  # if an exception/error occurred, do this
    print('ValueError happened. Sorry.')
except TypeError as type_error:
    # you can catch as many exceptions as you want. You
    # can give a name to the error
    print('TypeError happened. Sorry.')
else:  # (optional) this gets executed if the program tried and is successful.
    print(age)
finally:  # (optional) this gets executed every time (in success and failure cases)
    print('Finished')
