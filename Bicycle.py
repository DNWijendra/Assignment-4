class Bicycle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self.is_rented = False.

    def rent(self):
        self.is_rented = True
        return f"{self.brand} {self.model} is now rented."

    def return_bike(self):
        self.is_rented = False
        return f"{self.brand} {self.model} has been returned."