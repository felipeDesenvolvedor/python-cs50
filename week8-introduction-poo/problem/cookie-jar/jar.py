import sys

class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        self.quantity = 0

    def __str__(self):
        return self.print_cookie(self.capacity)
    
    def deposit(self, n):
        self._quantity = self._quantity + n

    def withdraw(self, n):
         if n > self._quantity:
             raise ValueError("Not enough cookies in the jar to withdraw.")
         self._quantity = self._quantity - n

    @property
    def _quantity(self):
        return self.quantity

    @_quantity.setter
    def _quantity(self, value):
        if value > self.capacity:
                raise ValueError(f"Cannot exceed the jar's capacity of {self.capacity} cookies.")
         
        self.quantity = value

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
        return self.print_cookie(self.quantity)

    def print_cookie(self, cookies):
        cookie = []
        
        for _ in range(cookies):
            cookie.append("🍪")
        return "".join(cookie)
         
         


def main():
    jar1 = Jar(6)
    jar1.deposit(4)

    print(jar1)

if __name__ == "__main__":
    main()