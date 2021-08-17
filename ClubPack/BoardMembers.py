# Module

class Boardmembers:
    def __init__(self, first_name, last_name, role):
        self.first_name = first_name
        self.last_name = last_name
        self.role = role

    def meet(self):
        print("Currently in a meeting...")


    def matchday(self):
        print("Match currently underway..")


    def press(self):
        print("Addressing the Press...")

