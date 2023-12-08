class Person:
    first_name = ""
    last_name = ""
    sex = ""
    drawed = None

    def __init__(self, first_name, last_name, sex):
        self.first_name = first_name
        self.last_name = last_name
        self.sex = sex

    def is_male(self):
        return self.sex == "male"

    def is_female(self):
        return self.sex == "female"

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def set_drawed(self, person):
        self.drawed = person
    