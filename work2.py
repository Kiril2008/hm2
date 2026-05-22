#1
class Student:
    def __init__(self, name, surname, group):
        self.name = name
        self.surname = surname
        self.group = group
        self.grades = []

    def add_grade(self, grade):
        self.grades.append(grade)

    def average(self):
        if len(self.grades) == 0:
            return 0
        return sum(self.grades) / len(self.grades)

    def is_excellent(self):
        return self.average() >= 90


s = Student("Kiril", "Semeniuk", "A1")

s.add_grade(95)
s.add_grade(90)
s.add_grade(85)

print(s.average())
print(s.is_excellent())


#2
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self._price = price
        self._quantity = quantity

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value >= 0:
            self._price = value

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        if value >= 0:
            self._quantity = value

    def sell(self, amount):
        if amount <= self._quantity:
            self._quantity -= amount
        else:
            print("Нехватає товару")

    def restock(self, amount):
        self._quantity += amount


p = Product("Laptop", 1000, 5)

p.sell(2)
print(p.quantity)

p.restock(10)
print(p.quantity)

p.price = -100
print(p.price)


#3
class MusicalInstrument:
    def __init__(self, name):
        self.name = name

    def play(self):
        print(self.name + " грає")


class Guitar(MusicalInstrument):
    def play(self):
        print(self.name + " грає на струнах")


class Piano(MusicalInstrument):
    def play(self):
        print(self.name + " грає мелодію")


class Drum(MusicalInstrument):
    def play(self):
        print(self.name + " б'є в барабани")


g = Guitar("Гітара")
p = Piano("Піаніно")
d = Drum("Барабан")

g.play()
p.play()
d.play()


#4
class PaymentMethod:
    def pay(self, amount):
        print("Оплата", amount)


class CreditCard(PaymentMethod):
    def pay(self, amount):
        print("Оплата карткою:", amount)


class PayPal(PaymentMethod):
    def pay(self, amount):
        print("Оплата через PayPal:", amount)


class CryptoCurrency(PaymentMethod):
    def pay(self, amount):
        print("Оплата криптою:", amount)


def process_payments(payments):
    for p in payments:
        p.pay(100)


payments = [
    CreditCard(),
    PayPal(),
    CryptoCurrency()
]

process_payments(payments)