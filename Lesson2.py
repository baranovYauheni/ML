import statistics as st


def filter_even(numbers):
    evens = [n for n in numbers if n % 2 == 0]
    return  evens

numbers = [1, 2, 3, 4, 5, 6]

def calculate_stats(numbers):
    total = st.median(numbers) + st.mean(numbers)
    return st.mean(numbers), st.median(numbers), total

kort = calculate_stats(numbers)

def greet_users(*names):
    for i in names:
        print(f"Hello {i}")

class Rectangle():
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def area(self):
        return self.height * self.width

    def perimetr(self):
        return 2 * (self.height * self.width)

    def is_square(self):
        return self.height == self.width

r1 = Rectangle(5,10)
r2 = Rectangle(7,7)

print("Площадь r1:", r1.area())
print("Периметр r1:", r1.perimetr())
print("r1 — квадрат?", r1.is_square())

print("_" * 10)

print("Площадь r2:", r2.area())
print("Периметр r2:", r2.perimetr())
print("r2 — квадрат?", r2.is_square())


class BankAccount():
    def __init__(self, balance = 0):
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Вы внесли {amount} лари. Текущий баланс равен {self.balance} лари")
        else:
            print("Баланс должен быть положительный")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Недостаточно средств")
        elif amount <= 0:
            print("Сумма должна быть полодительной")
        else:
            self.balance -= amount
            print(f"Вы сняли {amount} лари, текущий баланс равен: {self.balance} лари")

    def show_balance(self):
        print(f"Текущий баланс равен {self.balance} лари")


class SavingsAccount(BankAccount):
    def __init__(self, balance=0, interest_rate=0.05):
        super().__init__(balance)
        self.interest_rate = interest_rate  # процентная ставка (например, 5%)

    def add_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        print(f"Начислены проценты: {interest:.2f} ₽. Новый баланс: {self.balance:.2f} ₽.")


