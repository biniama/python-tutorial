class Student:
    """Class is like a house blueprint.
    Then, you can create as many Objects as you want"""

    def __init__(self, id, first_name, last_name, department, result):
        """assigning arguments from outside to self i.e. the Student"""
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.department = department
        self.result = result

    def full_name(self):
        """This concatenates first name and last name and returns the value"""
        return f'{self.first_name} {self.last_name}'
