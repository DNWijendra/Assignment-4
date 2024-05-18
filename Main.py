from bicycle import Bicycle
from customer import Customer

def main():
    # Create some bicycles
    bike1 = Bicycle("Trek", "Marlin 5")
    bike2 = Bicycle("Giant", "Talon 3")

    # Create a customer
    alice = Customer("Alice")

    # Customer rents a bike
    print(alice.rent_bike(bike1))

    # Customer returns a bike
    print(alice.return_bike(bike1))

if __name__ == "__main__":
    main()