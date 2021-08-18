class Bus:
    def __init__(self, **kwargs):
        self.brand = kwargs['brand']
        self.seat_count = kwargs['seat_count'] #int

    def __str__(self):
        return f'The bus name is {self.brand}'

    def theName(self):
        return print(f'The bus name is {self.brand}')

