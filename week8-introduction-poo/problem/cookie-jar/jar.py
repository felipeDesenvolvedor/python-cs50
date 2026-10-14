import sys

class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        self._quantity = 0

    def __str__(self):
        capacityCookie = []
        for _ in range(self.capacity):
            capacityCookie.append("🍪")
        return "".join(capacityCookie)
    
    def deposit(self, n):
        self.quantity = self.quantity + n

    def withdraw(self, n):
         if n > self.quantity:
             raise ValueError("Not enough cookies in the jar to withdraw.")
         self.quantity = self.quantity - n

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        if value > self.capacity:
                raise ValueError(f"Cannot exceed the jar's capacity of {self.capacity} cookies.")
         
        self._quantity = value

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, value):
        if value < 0:
            raise ValueError("Capacity must be a non-negative integer.")
        self._capacity = value

    @property
    def size(self):
            return self._quantity


def main():
    jar1 = Jar(5)

    jar1.deposit(5)
    jar1.withdraw(5)

    print(f"Quantity: {jar1.quantity}") 

if __name__ == "__main__":
    main()