#Module

class Physios:
    def __init__(self, first_name, last_name, physio_specialization, physio_salary):
        self.first_name = first_name
        self.last_name = last_name
        self.specialization = physio_specialization
        self.salary = physio_salary

    def help(self):
        print("Physio attending to player")